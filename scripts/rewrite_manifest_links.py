from __future__ import annotations

import argparse
import re
import shutil
import sys
import tarfile
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

MANIFEST_PATTERN = re.compile(
    r"https?://(?:www\.)?manifestdensity\.net[^\s<>'\"]+",
    flags=re.IGNORECASE,
)
DATE_PATTERN = re.compile(r"^:date:\s*(\d{4})-(\d{2})-(\d{2})", re.MULTILINE)
YEAR_FRAGMENT = re.compile(r"/(19|20)\d{2}/")
TRAILING_PUNCTUATION = ".,);:\"'!?]>\\"
DEFAULT_EXTENSIONS = (".rst", ".md", ".markdown", ".html", ".htm", ".txt")


@dataclass
class RewriteResult:
    replacement: str
    scenario: str


class TarAssetResolver:
    def __init__(self, archive_path: Path) -> None:
        self.archive_path = archive_path
        self.tar = tarfile.open(archive_path, "r:gz")
        self.index: dict[str, tarfile.TarInfo] = {}
        for member in self.tar.getmembers():
            if member.isfile():
                self.index.setdefault(Path(member.name).name.lower(), member)

    def has(self, filename: str) -> bool:
        return filename.lower() in self.index

    def extract(self, filename: str, destination: Path) -> None:
        member = self.index[filename.lower()]
        destination.parent.mkdir(parents=True, exist_ok=True)
        with self.tar.extractfile(member) as source, destination.open("wb") as target:
            if source is None:
                raise RuntimeError(f"Unable to extract {filename} from tarball")
            shutil.copyfileobj(source, target)

    def close(self) -> None:
        self.tar.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rewrite manifestdensity.net links in Pelican content by pointing to "
            "local copies or the running preview server."
        )
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path("content"),
        help="Root directory containing Pelican content (default: ./content)",
    )
    parser.add_argument(
        "--mirror-base",
        default="http://0.0.0.0:8080",
        help="Base URL for the migrated site to validate blog post links (default: http://0.0.0.0:8080)",
    )
    parser.add_argument(
        "--tar-archive",
        type=Path,
        help="Path to the legacy asset tar.gz for recovering missing files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze and report changes without modifying any files",
    )
    parser.add_argument(
        "--extensions",
        default=",".join(DEFAULT_EXTENSIONS),
        help="Comma-separated list of file extensions to inspect",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()

    return parser.parse_args()


def load_tar_resolver(tar_path: Optional[Path]) -> Optional[TarAssetResolver]:
    if tar_path is None:
        return None
    if not tar_path.exists():
        raise SystemExit(f"Tar archive {tar_path} does not exist")
    return TarAssetResolver(tar_path)


def extract_post_date(text: str) -> Optional[tuple[int, int, int]]:
    match = DATE_PATTERN.search(text)
    if not match:
        return None
    year, month, day = match.groups()
    return int(year), int(month), int(day)


def strip_trailing_punctuation(url: str) -> tuple[str, str]:
    trimmed = url.rstrip(TRAILING_PUNCTUATION)
    suffix = url[len(trimmed) :]
    return trimmed, suffix


def build_relative_url(parsed: urllib.parse.SplitResult) -> str:
    relative = parsed.path or "/"
    if parsed.query:
        relative = f"{relative}?{parsed.query}"
    if parsed.fragment:
        relative = f"{relative}#{parsed.fragment}"
    return relative


def check_mirror(
    original_url: str,
    parsed: urllib.parse.SplitResult,
    mirror_base: Optional[urllib.parse.SplitResult],
    cache: dict[str, Optional[str]],
) -> Optional[RewriteResult]:
    if mirror_base is None:
        return None
    if original_url in cache:
        cached = cache[original_url]
        if cached is None:
            return None
        return RewriteResult(cached, "mirror")

    candidate_paths = [parsed.path]
    if "_" in parsed.path:
        alt_path = parsed.path.replace("_", "-")
        if alt_path != parsed.path:
            candidate_paths.append(alt_path)

    for candidate_path in candidate_paths:
        target = urllib.parse.urlunsplit(
            (
                mirror_base.scheme or "http",
                mirror_base.netloc,
                candidate_path,
                parsed.query,
                parsed.fragment,
            )
        )
        status = request_status(target)
        if status is not None and status != 404:
            updated_parsed = parsed._replace(path=candidate_path)
            relative = build_relative_url(updated_parsed)
            cache[original_url] = relative
            return RewriteResult(relative, "mirror")

    cache[original_url] = None
    return None


def request_status(url: str) -> Optional[int]:
    headers = {"User-Agent": "manifest-link-rewriter/1.0"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=5) as response:
                return getattr(response, "status", 200)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return 404
            return exc.code
        except urllib.error.URLError:
            continue
    return None


def match_static_asset(
    parsed: urllib.parse.SplitResult, content_root: Path
) -> Optional[RewriteResult]:
    match = YEAR_FRAGMENT.search(parsed.path)
    if not match:
        return None
    fragment = parsed.path[match.start() :].lstrip("/")
    candidate = content_root / "static" / fragment
    if not candidate.exists():
        return None

    relative = f"/static/{fragment}"
    if parsed.query:
        relative = f"{relative}?{parsed.query}"
    if parsed.fragment:
        relative = f"{relative}#{parsed.fragment}"
    return RewriteResult(relative, "static")


def recover_from_tar(
    parsed: urllib.parse.SplitResult,
    tar_resolver: TarAssetResolver,
    date_info: Optional[tuple[int, int, int]],
    content_root: Path,
    dry_run: bool,
) -> Optional[RewriteResult]:
    if date_info is None:
        return None
    filename = Path(parsed.path).name
    if not filename:
        return None
    if not tar_resolver.has(filename):
        return None

    year, month, day = date_info
    relative_path = Path("static") / f"{year:04d}" / f"{month:02d}" / f"{day:02d}" / filename
    destination = content_root / relative_path
    if not dry_run:
        if not destination.exists():
            tar_resolver.extract(filename, destination)
    else:
        print(f"[dry-run] Would extract {filename} to {destination}")

    relative = "/" + str(relative_path).replace("\\", "/")
    if parsed.query:
        relative = f"{relative}?{parsed.query}"
    if parsed.fragment:
        relative = f"{relative}#{parsed.fragment}"
    return RewriteResult(relative, "tar")


def should_process(path: Path, content_root: Path, allowed_exts: set[str]) -> bool:
    if not path.is_file():
        return False
    if (content_root / "static") in path.parents:
        return False
    return path.suffix.lower() in allowed_exts


def process_file(
    path: Path,
    content_root: Path,
    mirror_base: Optional[urllib.parse.SplitResult],
    tar_resolver: Optional[TarAssetResolver],
    dry_run: bool,
    mirror_cache: dict[str, Optional[str]],
    allowed_exts: set[str],
    stats: dict[str, int],
) -> None:
    if not should_process(path, content_root, allowed_exts):
        return

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return

    if "manifestdensity.net" not in text.lower():
        return

    stats["files_scanned"] += 1
    date_info = extract_post_date(text)
    changed = False

    def repl(match: re.Match[str]) -> str:
        nonlocal changed
        original = match.group(0)
        url_body, suffix = strip_trailing_punctuation(original)
        parsed = urllib.parse.urlsplit(url_body)
        stats["links_found"] += 1

        result: Optional[RewriteResult] = check_mirror(
            url_body, parsed, mirror_base, mirror_cache
        )
        if result is None:
            result = match_static_asset(parsed, content_root)
        if result is None and tar_resolver is not None:
            result = recover_from_tar(parsed, tar_resolver, date_info, content_root, dry_run)

        if result is None:
            return original

        changed = True
        stats["rewritten"] += 1
        scenario_key = f"scenario_{result.scenario}"
        stats[scenario_key] = stats.get(scenario_key, 0) + 1
        print(f"{path}: {result.scenario} -> {url_body} -> {result.replacement}")
        return f"{result.replacement}{suffix}"

    new_text = MANIFEST_PATTERN.sub(repl, text)

    if changed:
        stats["files_modified"] += 1
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
    else:
        stats["unchanged_files"] += 1


def main() -> None:
    args = parse_args()
    content_root = args.content_root.resolve()
    if not content_root.is_dir():
        raise SystemExit(f"{content_root} is not a directory")

    mirror_base = urllib.parse.urlsplit(args.mirror_base) if args.mirror_base else None
    tar_resolver = load_tar_resolver(args.tar_archive)

    allowed_exts = {ext.strip().lower() for ext in args.extensions.split(",") if ext.strip()}

    stats: dict[str, int] = {
        "files_scanned": 0,
        "files_modified": 0,
        "links_found": 0,
        "rewritten": 0,
        "unchanged_files": 0,
    }

    try:
        mirror_cache: dict[str, Optional[str]] = {}
        for path in sorted(content_root.rglob("*")):
            process_file(
                path=path,
                content_root=content_root,
                mirror_base=mirror_base,
                tar_resolver=tar_resolver,
                dry_run=args.dry_run,
                mirror_cache=mirror_cache,
                allowed_exts=allowed_exts,
                stats=stats,
            )
    finally:
        if tar_resolver is not None:
            tar_resolver.close()

    print("\n--- Rewrite summary ---")
    print(f"Files scanned:   {stats['files_scanned']}")
    print(f"Files modified:  {stats['files_modified']}")
    print(f"Links found:     {stats['links_found']}")
    print(f"Links rewritten: {stats['rewritten']}")
    print(f"Mirror rewrites: {stats.get('scenario_mirror', 0)}")
    print(f"Static rewrites: {stats.get('scenario_static', 0)}")
    print(f"Tar rewrites:    {stats.get('scenario_tar', 0)}")
    if args.dry_run:
        print("Dry run complete: no files were modified.")


if __name__ == "__main__":
    main()
