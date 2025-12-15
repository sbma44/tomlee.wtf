from __future__ import annotations

import argparse
import csv
import re
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable

URL_PATTERN = re.compile(r"https?://[^\s<>'\"]+")
TRAILING_PUNCTUATION = ".,);:\"'!?]>\\"
DEFAULT_WORKERS = 12


def iter_files(content_root: Path) -> Iterable[Path]:
    for path in content_root.rglob("*"):
        if path.is_file():
            yield path


def extract_urls(text: str) -> list[str]:
    urls: list[str] = []
    for match in URL_PATTERN.findall(text):
        cleaned = match.rstrip(TRAILING_PUNCTUATION)
        urls.append(cleaned)
    return urls


def read_file(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_url(url: str, timeout: float = 10.0) -> str:
    last_error = "ERROR: UNKNOWN"
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(
            url,
            method=method,
            headers={"User-Agent": "tomlee-link-checker/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return str(response.status)
        except urllib.error.HTTPError as exc:
            return str(exc.code)
        except urllib.error.URLError as exc:
            reason = getattr(exc, "reason", exc)
            last_error = f"ERROR: URLError: {reason}"
        except Exception as exc:  # noqa: BLE001
            last_error = f"ERROR: {exc.__class__.__name__}: {exc}"
            break
    return last_error


def format_file_path(path: Path, content_root: Path) -> str:
    relative = path.relative_to(content_root)
    return str(Path(content_root.name) / relative)


def load_existing_statuses(csv_path: Path) -> dict[str, str]:
    statuses: dict[str, str] = {}
    if not csv_path.exists():
        return statuses
    try:
        with csv_path.open("r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            if not reader.fieldnames:
                return statuses
            if "url" not in reader.fieldnames or "status_code" not in reader.fieldnames:
                return statuses
            for row in reader:
                url = (row.get("url") or "").strip()
                status = (row.get("status_code") or "").strip()
                if url and status:
                    statuses[url] = status
    except Exception as exc:  # noqa: BLE001
        print(f"Warning: unable to reuse existing results: {exc}")
    return statuses


def main() -> None:
    parser = argparse.ArgumentParser(description="Check blog post links.")
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path("content"),
        help="Root directory containing posts (default: content)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("link_report.csv"),
        help="CSV file that will store the results",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help=f"Number of concurrent requests (default: {DEFAULT_WORKERS})",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=0,
        help="Limit checks to the newest N links for debugging (0 = all)",
    )
    args = parser.parse_args()

    content_root = args.content_root.resolve()
    if not content_root.is_dir():
        raise SystemExit(f"{content_root} is not a directory")

    output_path = args.output.resolve()
    status_cache = load_existing_statuses(output_path)

    entries: list[tuple[Path, str, float]] = []

    for file_path in iter_files(content_root):
        if file_path == output_path:
            continue
        text = read_file(file_path)
        if text is None:
            continue
        try:
            mtime = file_path.stat().st_mtime
        except OSError:
            mtime = 0.0
        urls = extract_urls(text)
        if not urls:
            continue
        seen_in_file: set[str] = set()
        for url in urls:
            if url in seen_in_file:
                continue
            entries.append((file_path, url, mtime))
            seen_in_file.add(url)

    if not entries:
        print("No URLs found.")
        return

    entries.sort(key=lambda item: (-item[2], str(item[0]), item[1]))

    if args.sample_size > 0:
        pending_entries: list[tuple[Path, str, float]] = []
        for entry in entries:
            if entry[1] in status_cache:
                continue
            pending_entries.append(entry)
            if len(pending_entries) >= args.sample_size:
                break
    else:
        pending_entries = [entry for entry in entries if entry[1] not in status_cache]

    urls_to_check = {url for _, url, _ in pending_entries}

    if urls_to_check:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            future_map = {
                executor.submit(check_url, url): url for url in sorted(urls_to_check)
            }
            for future in as_completed(future_map):
                url = future_map[future]
                result = future.result()
                status_cache[url] = result

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["url", "domain", "path", "status_code", "content_file"])

        for file_path, url, _ in entries:
            status = status_cache.get(url)
            if status is None:
                if args.sample_size > 0:
                    continue
                status = "UNKNOWN"
            parsed = urllib.parse.urlsplit(url)
            domain = parsed.netloc
            path = parsed.path or "/"
            if parsed.query:
                path = f"{path}?{parsed.query}"
            content_file = format_file_path(file_path, content_root)
            writer.writerow([url, domain, path, status, content_file])


if __name__ == "__main__":
    main()
