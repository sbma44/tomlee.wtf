for no good reason this is making me angry about the iPad
#########################################################
:date: 2010-04-03 14:17
:author: admin
:category: Uncategorized
:slug: for-no-good-reason-this-is-making-me-angry-about-the-ipad
:status: published
:save_as: 2010/04/03/for-no-good-reason-this-is-making-me-angry-about-the-ipad/index.html
:url: 2010/04/03/for-no-good-reason-this-is-making-me-angry-about-the-ipad/

This will interest nobody, but I need to complain (and perhaps spare others some fruitless googling): the iPhone version of Safari seems to be broken when using AJAX in offline caching in HTML5 applications.

"Why would you want to use AJAX in an offline app?" you ask, and it's a good question. Well, I'm trying to make an HTML5 interface to the `office door-opening thingy <http://sunlightlabs.com/blog/2010/our-door-opener-science-project/>`__, because the native iPhone version, being a non-App Store offering, will be expiring soon in an irritating way (insert entirely different anti-Apple rant here).

Users will, of course, need network access to open the door. But I don't see any particular reason to make users download the 300-some-K of assets necessary to make a proper `jQTouch <http://www.jqtouch.com/>`__ iPhone app work every time they need to get into the office (or change their settings) -- particularly since I'm using a little onSuccess wav file (just for fun). So I set about using some offline caching to keep all that material decidedly on the iPhone, and not subject to the whims of Safari's caching policy.

This works fine until it's time to issue the request to open the door. The cache manifest file, which allows you to specify which items will be stored offline, allows for a whitelisted "NETWORK" section that will never be subject to the cache. Typically, you add your AJAX endpoint(s) to that section. Except in this case that AJAX request is made to a different domain than the one where the application lives (and when the application is being served from an offline cache who knows where it \*thinks\* it lives?), utilizing the now years-old-but-still-awfully-clever `JSONP <http://en.wikipedia.org/wiki/JSONP>`__ to escape the same-domain restrictions of a vanilla AJAX request.

This all works fine, `according to other people <http://stackoverflow.com/questions/1911614/how-do-i-avoid-having-jsonp-returns-cached-in-an-html5-offline-application/2572077>`__. But not for me. My application's endpoint uses SSL in order to protect users' door-opening credentials, and that seems to make the difference. It just. doesn't. work. If you change the cache manifest, prompting the app to be reloaded, everything will work fine. Once. When you reload the app, pulling from the offline cache, the AJAX request produces a momentary activity indicator in the status bar, but there's no response. (No error, either! Thanks a bunch, Apple and/or jQuery.)

I've tried `updating jQuery <http://code.google.com/p/jqtouch/issues/detail?id=179>`__. I've tried whitelisting "\*". I've tried whitelisting the http version of the endpoint, and just the path portion of the endpoint, and the full domain name of the endpoint (SSL and not). No dice.

Here's the relevant code, for anyone feeling particularly curious/masochistic. I've tried a lot of variations on it -- at this point I'm pretty sure that this aspect of iPhone Safari circa OS 3.1.2\* is just broken. Ah well. No caching isn't the end of the world, but it is kind of annoying.

| [cc lang="javascript"]// I've tried it with and without the callback param (as I go back and forth between $.getJSON and $.ajax) -- doesn't make a difference
| var url = 'https://gatekeeper.sunlightlabs.com/[SECRET]/api/?device_id=' + localStorage.deviceID + '&pin=' + PIN + '&format=json&callback=?';

| $.ajax({
| url: url,
| dataType: 'jsonp',
| error: function(XMLHttpRequest, textStatus, errorThrown){
| alert(textStatus); // this never happens
| },
| success: function(data){
| localStorage.message = 'Welcome, ' + data.first_name + '!';
| localStorage.lastOpen = (new Date()).getTime();
| if(localStorage.disableSound=='on')
| {
| alert(localStorage.message);
| localStorage.message = '';
| }
| else
| {
| location.href = 'zelda.wav'; // play the zelda door-opening music on success
| }
| }
| });[/cc]

\* Gotta keep that tethering
