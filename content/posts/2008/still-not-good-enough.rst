still not good enough
#####################
:date: 2008-10-28 17:44
:author: admin
:category: tech
:slug: still-not-good-enough
:status: published
:save_as: 2008/10/28/still-not-good-enough/index.html
:url: 2008/10/28/still-not-good-enough/
:private: true

Another day, `another music-sharing flash widget that uses RC4 to encrypt its MP3 URLs but keeps the key in the SWF <http://www.playlist.com/>`__.

I realize I've never made good on `my promise to explain how I would build a secure Flash music player </2008/03/28/surprisingly-i-dont-consider-myself-a-jerk/>`__. Partly I forgot; partly it's just that it's an impossible problem, and proposing incremental improvements to the situation isn't very satisfying.

But look, you can at least half-ass it. Right now if someone gets a hold of the MP3 URL the jig is up — they can repost it anywhere else and help themselves to your bandwidth. You can improve on this situation, at least, by serving a dynamic playlist filled with URLs that are only good for the current user. Either throw each URL away after one use (admittedly problematic for repeating a song without additional trips to the playlist server); or, better yet, find the song by hashing its unique identifier together with the user's IP and user agent (again, in the dynamic playlist generation script). You don't have to move any files around, you just have to write a script that looks up the requested hash in the database and then pipes out the MP3 from its secret location. There's no need for encryption, even. Season with additional querystring parameters and column indices to taste.

"But Tom!" you cry, "Can't an enterprising jerk like yourself then write a script that reverse-engineers this process and automatically creates URLs that are compatible with their use agent/IP combination?" Well, yes — although the salting algorithm (and song identifier, potentially) will remain secret, so you're going to need a rainbow table, which usually costs money. But also no, because you made a note in your database when the browser talked to the playlist server. So strangers can't come in — they have to have at least asked for that playlist first.

Of course, if they went after the MP3 they would done so have, anyway. So yes, securing the file against individuals is still hopeless — I hope I never implied otherwise. But at least reposting or emailing the link won't get them anywhere.

The downside to all of this is that you're going to have to stop using a big dumb CDN. But look, it's just not that hard to stand up a dead-simple EC2 LAMP instance to serve your playlist creation script and pipe stuff out of S3. `Elasticfox <http://developer.amazonwebservices.com/connect/entry.jspa?externalID=609>`__, people.

Oh, and one other thing: for god's sake, ban jackasses like me the first time you see a naked curl user-agent string. I never remember that -A flag until I absolutely have to.
