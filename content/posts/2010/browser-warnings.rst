browser warnings
################
:date: 2010-03-18 14:23
:author: admin
:category: tech
:slug: browser-warnings
:status: published
:save_as: 2010/03/18/browser-warnings/index.html
:url: 2010/03/18/browser-warnings/
:private: true

`Kevin Drum elects to take security advice from Microsoft <http://motherjones.com/kevin-drum/2010/03/you-and-your-browser>`__. This is not a good idea!

In a nutshell: MS says that users ignore warnings about unsigned encryption keys, which makes those warnings useless.  Some browsers, like Firefox, make it *really difficult* to ignore unsigned keys, but that's annoying, and MS says we should abandon such efforts.

This is wrong.  Those warnings are saying: "The URL you entered means that you've asked for a snoop-proof connection, so okay, your connection to this server is encrypted; however, *I can't verify that this server is who it's claiming to be*."  Your conversation with the server will be private, but you could be subject to a so-called man-in-the-middle attack, whereby someone hijacks the local network segment you're on and starts speaking on behalf of, say, bankofamerica.com.  The magic of the certificate authority system means that they can't do this without generating a warning.

There is one caveat: if they simply don't try to use encryption, the warning won't be generated.  This is one of the reasons why you're supposed to check for https:// in the URL whenever you submit sensitive information; not just so that your password isn't available to everyone else on the Bolt Bus (though that's a good reason, too), but also so that anyone pretending to be a server they're not will get caught.  Unfortunately, people aren't very good at checking for that little s in the URL or that little key icon or whatever other little security indicator your browser provides, so the bad guys just direct their victims to unsecured sites.

That's too bad, but it isn't a sign that warnings about unsigned keys are bad ideas.  Actually, the fact that phishers have drifted away from that link in the security chain means that *it's working properly*.  Weakening it isn't any kind of solution.  MS security researchers would be better-served by spending more time thinking about how to get people to notice when they ought to be using a secure site.
