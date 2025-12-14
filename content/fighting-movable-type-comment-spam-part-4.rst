fighting movable type comment spam - part 4
###########################################
:date: 2007-01-29 01:29
:author: admin
:category: tech
:slug: fighting-movable-type-comment-spam-part-4
:status: published
:save_as: 2007/01/29/fighting-movable-type-comment-spam-part-4/index.html
:url: 2007/01/29/fighting-movable-type-comment-spam-part-4/

Okay. Last one, I promise. Now that you've gone through all of these steps, here are the things that you probably should have tried before listening to me:

- `Ben <http://www.unfogged.com/archives/week_2006_06_11.html#005044>`__'s querystring-based twist on JS obfuscation has apparently been highly successful. It's simple and clever — give it a try. It also makes me realize that my rotating-mt-comments solution could've been implemented with .htaccess files, eliminating the need for FTP nonsense and allowing us to avoid making changes to mt-config.cgi. That'd be a better way to do it, but the benefits aren't enough to make me rewrite the script. Plus, not everyone has mod_rewrite enabled, so the original solution will work on slightly more systems.
- `MT-Akismet <http://appnel.com/kb/mtakismet/mtakismet-manual>`__ is a Movable Type plugin that brings the power of `Wordpress <http://www.wordpress.org>`__'s Akismet spam-blocking system to MT. I installed it a few weeks ago and it seems to have helped, although in my case it didn't completely eliminate the flow of spam. Considering that I don't get all that much comment spam at this domain, that makes me disinclined to pimp MT-Akismet as a magic bullet. But it seems to do something, and does so without needing supervision. Also, lots of people swear by it. You might as well give it a try.
- `Captchas <http://www.sixapart.com/pronet/plugins/plugin/captcha.html>`__ are probably the most foolproof method of stopping spam. But users don't like them, and in my experience they're a pain in the ass to install. Still, if you want to stymie the spammers, this is probably the best way to do it.
- There's always TypeKey, MT's unified login solution. In my experience, it's `terrible <http://www.dcist.com/archives/2006/01/04/typekeys_reign_1.php>`__. Admittedly, the situation at DCist was worse than normal because Gothamist's server architecture meant that comments had to be submitted across a few different domain names, which made TypeKey's cookies go crazy. But overall, I came away deeply unimpressed.
- Finally, there are a `couple <http://www.sixapart.com/pronet/plugins/plugin/closecomments.html>`__ of `plugins <http://www.sixapart.com/pronet/plugins/plugin/conversation_ki.html>`__ that will close comments on older entries. There are downsides — people wandering in from Google won't be able to leave their thoughts on your old entries — but if you don't mind them, it should help.
