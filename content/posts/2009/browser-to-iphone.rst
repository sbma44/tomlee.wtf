making it easier to move from the browser to the iPhone
#######################################################
:date: 2009-07-24 11:32
:author: admin
:category: tech, Uncategorized
:slug: browser-to-iphone
:status: published
:save_as: 2009/07/24/browser-to-iphone/index.html
:url: 2009/07/24/browser-to-iphone/
:private: true

Although it is arguably as much a business innovation as a technological one, there's no doubt that the iPhone has radically altered the mobile device landscape, and, in the process, profoundly changed the way that Americans think about sitting on the toilet.

In fact, its uses extend beyond this crass but foremost example.  You've also got your standing-in-line downtime, the crucial waiting-for-coffee-to-brew period, and of course miscellaneous hours spent idly fiddling while in meetings. If I'm not mistaken, the Bureau of Labor Statistics is on record as saying that high scores from Sudoku games played on mobile devices account for most of the productivity gains of the past decade.

Personally, I like to use the device to catch up on my online reading.  But this crucial electronic-fucking-around is slowed by the need to enter URLs.  If you're like me, typically you'll have some long-form article open in a neglected browser tab: say, 2000 words from Sasha Frere-Jones on why your implicit acceptance of the latest top 40 hit means you're more -- and less! -- racist than you thought.  It's something I mean to read, but which the demands of the workday have made me put off.  As I leave my desk to pursue less productive activities (food acquisition; interaction with humans), I frequently find myself wishing I had that article loaded on my handset.  But the only way to move it there without tedious typing is to email myself the link, then check my email, then click on the link.  If only there was an almost perfectly equivalent but slightly faster way!

Well, you're/I'm in luck!  I twittered this ridiculous first-world complaint the other day, and @tbridge and @jroo helpfully pointed me toward `Prowl <http://prowl.weks.net/>`__, a $2.99 iPhone app that takes the 3.0 firmware's push notification capabilities and wraps them in a simple API.

This opens the door to creating a bookmarklet that grabs your browser's current URL and pushes it to your phone.  The phone will buzz, you'll click the "view" button, and you can then follow the link.  Easy!  Here's the bookmarklet.  Just follow these steps (which, I should note, have only been tested in Firefox 3.5):

#. Buy Prowl.  Open it on your iPhone -- you'll need to register with its parent site and give the app permission to display notifications.
#. Using your newly-created credentials, log into the Prowl site. Go to the settings tab and create an API key by clicking the appropriate button.
#. Paste the API key into the form field below. Click the "Create Bookmarklet" button. NOTE: the customization of the bookmarklet is done in client-side Javascript, entirely within your browser -- don't worry, you won't be sending me your API key.
#. Drag the newly-created button into your browser's quicklaunch bar.

Simple!  Now when you click that bookmarklet a new window will be briefly opened.  It'll submit a request to the Prowl site that contains the current URL that you're looking at.  Shortly thereafter you should get a message on your phone with the link.

.. container::

   .. raw:: html

      </p>

   .. container::
      :name: bkmklt

      |Send it to my screen!|

.. raw:: html

   <p>

.. raw:: html

   <script type="text/javascript">// <![CDATA[<br />
   jQuery(function(){<br />
      jQuery('#createbkmklt').click(function(){<br />
         jQuery('a#bkmklt-link').attr('href', jQuery('a#bkmklt-link').attr('href').replace('__APIKEY__', jQuery('#apikey').val()));<br />
         jQuery('a#bkmklt-link img').show();<br />
      });<br />
   });<br />
   // ]]></script>

.. raw:: html

   </p>

As for the new window: I admit, it's inelegant to spawn a popup.  But the Prowl API only accepts POSTed requests, which, barring a sudden and deeply unwise decision on their part to host third-party scripts, rules out a more seamless AJAX solution.  The popup works well enough, although on especially slow connections the window may wind up closed before the request goes through.  A better solution would involve a timer that checks the spawned window for when its location.href property suddenly becomes inaccessible due to cross-domain security policies (indicating that the page it contains is now being served by the Prowl domain).  But my first crack at that didn't work, so for now you guys are stuck with this.

.. |Send it to my screen!| image:: /static/2009/07/sendittomyscreen.png
   :target: javascript:f=function()%7Bvar%20w=window.open(%22%22,%22wildebeast%22,%22width=30,height=30,scrollbars=0,resizable=1%22);var%20url=window.location.href;var%20html%20=%20%27%3Chtml%3E%3Chead%3E%3C/head%3E%3Cbody%3E%3Cform%20action=%22https://prowl.weks.net/publicapi/add%22%20method=%22POST%22%3E%3Cinput%20type=%22hidden%22%20name=%22apikey%22%20value=%22__APIKEY__%22%20/%3E%3Cinput%20type=%22hidden%22%20name=%22priority%22%20value=%220%22%20/%3E%3Cinput%20type=%22hidden%22%20name=%22application%22%20value=%22CTU%22%20/%3E%3Cinput%20type=%22hidden%22%20name=%22event%22%20value=%22Chloe%20says:%22%20/%3E%3Cinput%20type=%22hidden%22%20name=%22description%22%20value=%22%27%20+%20url%20+%20%27%22%20/%3E%3C/form%3E%3Cscript%20type=%22text/javascript%22%3Edocument.forms%5B0%5D.submit();%3C/script%3E%3C/body%3E%3C/html%3E%27;w.document.open();w.document.write(html);w.document.close();window.setTimeout(function()%7B%20w.close();%20return%20false;%7D,%20500);%7D;f();
