last year's model
#################
:date: 2007-07-24 15:52
:author: admin
:category: tech
:slug: last-years-model
:status: published
:save_as: 2007/07/24/last-years-model/index.html
:url: 2007/07/24/last-years-model/
:private: true

There are too many folks competing in this year's MediaBistro beauty pageant for me to take sides. But I'm always eager to convince my friends to learn some scripting mojo (seriously, it'll make your life better). So here's the code that worked last year. How to configure it, modify it, and run it is left as an exercise for the reader.

   ::

      #!/usr/bin/perl
      use WWW::Mechanize;
      my $num_votes_to_make = 9999; # this would be a bit obvious, wouldn't it?
      my $min_sleep_time = 1; # sleep at least a second between votes
      my $max_sleep_time = 10; # but no more than ten seconds
      my $mech = WWW::Mechanize->new();
      $mech->proxy(['http', 'ftp'], 'http://127.0.0.1:8118/'); # use a Tor proxy on port 8118 to hide our IP address (http://tor.eff.org)
      for(my $i=0;$i<$num_votes_to_make;$i++)
      {
      print "voting...\n";
      my $url = 'http://mediabistro.com/articles/poll/000091/';
      $mech->get( $url );
      $mech->submit_form(
      form_number => 0,
      fields => {
      rsld => '330'
      }
      );
      my  $random_sleep_time = int(rand( $max_sleep_time-$min_sleep_time+1 ) ) + $min_sleep_time;
      print "sleeping " . $random_sleep_time . " seconds...\n";
      sleep $random_sleep_time;
      }
