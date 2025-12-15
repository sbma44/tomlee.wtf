Muxtape unraveled
#################
:date: 2008-03-27 21:31
:author: admin
:category: music, tech
:slug: muxtape-unraveled
:status: published
:save_as: 2008/03/27/muxtape-unraveled/index.html
:url: 2008/03/27/muxtape-unraveled/
:private: true

I've seen a lot of attention paid to `Muxtape <http://www.muxtape.com>`__ over the past few days, and I agree: it's nice! I think a lot of the romanticism that people attach to the mixtape format is silly, and that removing portability from the equation makes it a lot less useful. But Muxtape is clean and built around an attractively simple idea.

I will say, though, that it does even less than usual to prevent the files it stores from being downloaded. If you fire up Firebug after you start a song playing, it's easy enough to find the Flash player, which is being passed a set of parameters that look like this:

   type=mp3&width=0&height=0&file=http%3A//muxtape.s3.amazonaws.com/songs/abcdefg94fb3f63d668bbc521b8eb3460%3FPLEASE%3DDO_NOT_STEAL_MUSIC%26AWSAccessKeyId%3D1R7VFFT45XS0N28M1K02%26Expires%3D1206670309%26Signature%3Dl8pKlxHGgz2LdSomiK38sA%252Fp7EM%253D&javascriptid=playeraa5bd894fb3f63d668bbc521b8eb3460&enablejs=true

If you pull out the *file* parameter and decode it, it looks like this:

   http://muxtape.s3.amazonaws.com/songs/abcdefg94fb3f63d668bbc521b8eb3460?PLEASE=DO_NOT_STEAL_MUSIC

Yes, really. I've changed enough of the URL to make it invalid, but still: asking is probably not going to be enough.

I'll admit that this is a hard problem to solve. Unless you're prepared to undertake a major software development project whereby you decrypt your data client-side and send raw PCM to the sound card — and trust me, you're probably not — you're going to be stuck using Adobe Flash to play music in-browser. And if that's the case, you're pretty much stuck using a command that amounts to:

   dear_flash_please_play_this_mp3('http://server.com/my-music-file.mp3');

This is not very secure — Flash needs to get that URL from somewhere, and if the user can figure it out they can download the file as easily as Flash can. All you can do at THAT point is hiding the name of the file by changing it so quickly that a user's browser can be bothered to figure it out, but the user herself cannot (this is what iMeem and MySpace do). You'll probably also insert some hoops that Flash has to jump through to prove its Flash-iness, all of which can be easily faked but which will at least discourage casual downloading.

But the guy running Muxtape has screwed himself out of these measures by using Amazon S3 to store his files, which is handy and cheap but can't implement a system for changing filenames rapidly, or employ HTTP user agent filtering, or check for tokens, or really do any other server-side cleverness. So the only option he has left is simply asking people not to download. Which I admire, because all of these countermeasures, even the encryption, can be defeated. But I doubt the record companies are going to be as sanguine about it.

But who knows! Maybe he'll be able to figure out some sort of promotional detente the way the Hype Machine folks have. I hope so. But right now it will be pretty easy for someone to write a Greasemonkey script to allow direct downloading, or for music bloggers looking for free storage to hotlink the site to death.
