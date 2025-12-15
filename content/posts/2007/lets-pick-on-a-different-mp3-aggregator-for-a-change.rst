let's pick on a different mp3 aggregator for a change
#####################################################
:date: 2007-11-26 16:14
:author: admin
:category: music, tech
:slug: lets-pick-on-a-different-mp3-aggregator-for-a-change
:status: published
:save_as: 2007/11/26/lets-pick-on-a-different-mp3-aggregator-for-a-change/index.html
:url: 2007/11/26/lets-pick-on-a-different-mp3-aggregator-for-a-change/
:private: true

The Hype Machine is great, but it's not the only one out there, after all. Besides, it's got certain shortcomings: its "popular" page is fine if you want to listen to a ton of Bloc Party, but can suffer from a lack of variation. And looking at the front page is like drinking from a firehose. The `podcast feed that I made last week </2007/11/23/everything-is-connected/>`__ suffers for it: you're not getting a representative snapshot of what's being talked about, but rather just a random sampling of what was popular when your copy of iTunes decided to check in. And, as I mentioned, the feed will no doubt be shut down by the HM guys (they may have already throttled iTunes' bandwidth).

So what about elbo.ws? They publish a `daily-updated list of popular tracks <http://elbo.ws/tracks>`__ that contains more music I haven't heard. And it's persistent enough that querying it once a day could be useful. The only problem is that it doesn't carry any MP3 links: users have to go hunting at the linked blogs to find links that are still alive. This makes it kind of a pain in the ass to check out the referenced music (and is why I generally prefer the Hype Machine).

But it *is* possible to create a podcast feed using techniques similar to the ones I applied to the Hype Machine. `Here's <http://pipes.yahoo.com/sbma44/elbowspodcast>`__ a pipe that simply retrieves the elbo.ws top tracks feed (or any other elbo.ws feed — it just defaults to that) and adds an enclosure tag to each entry. That tag tells iTunes (or whatever) to come talk to my server, passing the link associated with the elbo.ws entry.

At the server the request is intercepted via an .htaccess rewrite rule and redirected to a script (iTunes insists on URLs ending in .mp3, otherwise this would be unnecessary). The script pulls up the elbo.ws page and grabs the song name and listed blogs. It then loads the blogs and pulls out all of the MP3 links. From there it compares the link text to the collected song name and orders the results by similarity scores. Then it attempts to load each URL. For the first working one it finds it sends a redirect message to iTunes.

All this text processing and page-loading is pretty computationally expensive — it generally takes about half a minute to find a match — but with some caching it my server shouldn't be *completely* destroyed. An occasional incorrect match is returned, but overall I'm pretty pleased with the thing.

Here's the code for anyone interested. Given that this doesn't affect the elbo.ws folks' bandwidth or liability, I'm assuming they won't mind:

   ::

      <?php
      // taken from http://www.php.net/manual/en/function.file-exists.php#79118
      function url_exists($url)
      {
      $handle   = curl_init($url);
      if (false === $handle)
      {
      return false;
      }
      curl_setopt($handle, CURLOPT_HEADER, false);
      curl_setopt($handle, CURLOPT_FAILONERROR, true);
      curl_setopt($handle, CURLOPT_NOBODY, true);
      curl_setopt($handle, CURLOPT_RETURNTRANSFER, false);
      $connectable = curl_exec($handle);
      curl_close($handle);
      return $connectable;
      }
      function get_url($location)
      {
      $ch = curl_init($location);
      curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
      curl_setopt($ch, CURLOPT_HTTPHEADER, array('Connection: close'));
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
      curl_setopt($ch, CURLOPT_TIMEOUT, 15);
      $response = curl_exec($ch);
      curl_close($ch);
      return $response;
      }
      function usort_by_similarity($a,$b)
      {
      if($a['similarity']==$b['similarity'])
      return 0;
      else
      return (($a['similarity']>$b['similarity']) ? 1 : -1);
      }
      function get_mp3_link_uncached($elbows_url)
      {
      $blog_matches = array();
      $elbows_page_id = preg_replace('/^.*#/','',$elbows_url);
      $elbows_page_html = get_url($elbows_url);
      $blog_links = array();
      if(preg_match_all('/<ul[^>]*>.*?<\/ul>/i',$elbows_page_html,$elbows_page_unordered_lists,PREG_SET_ORDER))
      {
      $matching_ul_html = '';
      foreach($elbows_page_unordered_lists as $match)
      {
      if(stristr($match[0],$elbows_page_id))
      $matching_ul_html .= $match[0];
      }
      preg_match_all('/href=[\'"](.*?)[\'"]/',$matching_ul_html,$blog_matches,PREG_SET_ORDER);
      $song_name = $elbows_page_id;
      if(preg_match_all('/<h3[^>]*>(.*?)<\/h3>/',$elbows_page_html,$song_name_matches,PREG_SET_ORDER))
      $song_name = $song_name_matches[0][1];
      }
      $matches_for_analysis = array();
      foreach($blog_matches as $match)
      {
      // find all mp3 links on the blog page
      $html = get_url($match[1]);
      if(preg_match_all('/<a[^>]+href=[\'"]([^\'"]*?\.mp3)[\'"][^>]*>(.*?)<\s*\/a\s*>/i',$html,$mp3_matches,PREG_SET_ORDER))
      {
      // retrieve the one with the most similar inner text and store it for more processing
      $current_best_match = null;
      foreach($mp3_matches as $mp3_match)
      {
      $l_similarity = levenshtein(substr($mp3_match[2],0,255), substr($song_name,0,255));
      if((!is_array($current_best_match))||($current_best_match['similarity']>$l_similarity))
      {
      $current_best_match = array(
      'url' => $mp3_match[1],
      'text' => $mp3_match[2],
      'similarity' => $l_similarity,
      );
      }
      }
      if($current_best_match!=null)
      {
      $matches_for_analysis[] = array(
      'url' => $current_best_match['url'],
      'text' => $current_best_match['text'],
      'similarity' => $current_best_match['similarity'],
      );
      }
      }
      }
      // sort the matches list from all blogs to find the one with the most similar title
      usort($matches_for_analysis,'usort_by_similarity');
      for($i=0;$i<sizeof($matches_for_analysis);$i++)
      if(url_exists($matches_for_analysis[$i]['url']))
      return $matches_for_analysis[$i]['url'];
      }
      if(isset($_GET['url']))
      {
      ini_set('max_execution_time',999999);
      ini_set('include_path','.:/usr/lib/php:/usr/local/lib/php:/include:/home/metamon/php');
      require_once('Cache/Function.php');
      define('CACHE_EXPIRATION_IN_SECONDS',900);
      $fcache = new Cache_Function('file', array('cache_dir' => './cache', 'filename_prefix' => 'fcache_elbows_'), CACHE_EXPIRATION_IN_SECONDS);
      $mp3_url = $fcache->call('get_mp3_link_uncached',urldecode($_GET['url']));
      header("HTTP/1.1 301 Moved Permanently");
      header("Location: " . $mp3_url);
      exit();
      }
      ?>

And the .htaccess looks like this:

   ::

      <IfModule mod_rewrite.c>
      RewriteEngine on
      RewriteRule ^.*\.mp3(.*)$ index.php$1 [L,QSA]
      </IfModule>

I should add that I know none of this is new or mindblowing — projects like `Songbird <http://www.songbirdnest.com/>`__ are designed for exactly this sort of thing. But I like having my iPod automatically sync from one place, and I wanted to get at the elbo.ws feed specifically. Plus, y'know, it was fun to figure this out — it certainly taught me some things about the limits of Yahoo Pipes' JSON functionality.
