a little more on migrating from Typepad to Movable Type
#######################################################
:date: 2007-08-27 10:42
:author: admin
:category: tech
:slug: a-little-more-on-migrating-from-typepad-to-movable-type
:status: published
:save_as: 2007/08/27/a-little-more-on-migrating-from-typepad-to-movable-type/index.html
:url: 2007/08/27/a-little-more-on-migrating-from-typepad-to-movable-type/

I realized I might as well post this script, too. Say you're moving from one host to another, and the source exports to the MT/Typepad format (a big long text file) and the new host can read that format (`Wordpress can <http://wordpress.org/docs/tutorials/import-mt/>`__, and of course MT/Typepad can).

You're facing a problem: your entries' text is probably littered with images and links pointing at your old domain. Those links are presumably going to become dead sometime after the transition; you'd like to rewrite them to point at the new domain. You'd also like to download any images, PDFs or other digital assets that they point to, then upload them to the new server.

Well, here's a script that you can run against the exported MT/Typepad file:

   ::

      #!/usr/bin/perl
      my $url, $rewritten_url;
      while(my $l = <>)
      {
      while($l =~ m/(href|src)=['"](http:\/\/beutler\.typepad\.com\/.*?)['"]/i)
      {
      $url = $2;
      $rewritten_url = $url;
      $rewritten_url =~ s/http:\///igx;
      if($url =~ m/\.(html?|php)/i)
      {
      $rewritten_url =~ s/^\/beutler\.typepad\.com\/home//igx;
      $rewritten_url =~ s/\.(html?|php)$/\//i;
      }
      else
      {
      my $prefix = $rewritten_url;
      $prefix =~ s/^\///;
      $prefix =~ s/\/[^\/]+$//;
      `wget -q --directory-prefix=$prefix $url`;
      }
      $l =~ s/$url/$rewritten_url/gx;
      }
      print $l;
      }

If you saved this file as *rewrite_entries.pl*, you'd run it like so:

   ::

      cat MT_EXPORT_FILE.txt | ./rewrite_entries.pl > MT_EXPORT_FILE_REWRITTEN.txt

You'd end up with a new text file (which is the one you should import) and a subdirectory full of images and PDFs that you'll want to FTP up to your new server. There's some Brian-specific stuff in the above script, but it shouldn't take very much work to adapt it to a different site.
