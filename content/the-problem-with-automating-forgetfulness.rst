the problem with automating forgetfulness
#########################################
:date: 2007-05-16 18:10
:author: admin
:category: tech
:slug: the-problem-with-automating-forgetfulness
:status: published
:save_as: 2007/05/16/the-problem-with-automating-forgetfulness/index.html
:url: 2007/05/16/the-problem-with-automating-forgetfulness/

Last week I used Viktor Mayer-SchÃ¶nberger's `"Useful Void" proposal <http://www.vmsweb.net/attachments/pdf/Useful_Void.pdf>`__ (PDF) as a jumping-off point to ruminate about Facebook, the work/personal divide and darknets over `here <http://www.manifestdensity.net/2007/05/10/the_internet_is_like_an_electr/>`__. Along the way I casually dismissed Mayer-SchÃ¶nberger's proposal:

   I'm sure his heart is in the right place, but this is dumb for all the same reasons that DRM is dumb. You really, really can't control the spread or persistence of publicly available digital information. Efforts to do so are a waste of everyone's time.

But then, much to my surprise, the man himself popped up in comments, leaving this polite note:

   | You seem to suggest that my proposal is similar to IP secured by DRM. It seems that you haven't actually looked at my paper. In the paper I suggest that a DRM-like approach (as Lessig has made in Code 2.0) would be overkill. What I desire is not perfect solution, just a shift in defaults that makes users think again about the choice of forgetting.
   | I encourage you to read the paper - it's a free download, including from my `website <http://www.vmsweb.net/>`__, and I think addresses some of the concerns you seem to have.
   | In contrast your solution (cognitively accepting the fact that we are transparent and thus weigh things differently) depends on our brains ability to adapt - not something that cognitive scientists have much hope in I am afraid, espcially since biologically we are wired to forget.
   | Kind regards,
   | VMS

Well, guilty as charged — I hadn't read his proposal. But now I have, and I'm afraid that I still arrive at much the same conclusion: I think that it probably isn't workable, and it definitely wouldn't be wise.

His proposal specifically involves the legislative mandating of a system of expiration metadata that would be built into software. It could be easily overridden by data creators when necessary — your Word documents won't start disappearing — but by default data would be "forgotten" after a set period of time.

But how did we get into the situation we're currently in, with huge amounts of data being acquired? As Mayer-SchÃ¶nberger points out, storage is very cheap. But it's not free — data is still retained for one of two reasons: either people assign *value* to the data, or the costs associated with throwing it away (and sifting out what shouldn't be thrown away) exceed the cost of storing it.

The proposal may help with the second situation. Introducing statutory penalties raises the cost of retaining data, which may spur organizations to throw it away. Of course, the cost of throwing away data isn't made any cheaper by the system, but presumably Mayer-SchÃ¶nberger thinks it's worthwhile to introduce that inefficiency.

The first situation is unlikely to be helped, however. If a user assigns value to a piece of data — i.e. they think it's useful or may become useful in the future — there's very little that one can do to stop them from retaining it indefinitely. Data doesn't just delete itself, after all. To make sure it disappears at a set time you can do one of two things: either design a system that simply refuses to read a piece of data after the expiration date, or one that actively collects and deletes content on or near the expiration date. The first option involves per-use permissioning — simply put, it's DRM, and just as difficult to implement effectively. The second system relies on the creation and maintenance by the user of systems designed to destroy data they want to keep. Unless Trusted Computing becomes a reality, that's not likely to happen — and even then, what could you do about physical media like DVDs?

Besides, there's a downside to this proposal: driving data archiving underground (so to speak) would lead to great losses in utility. Suppose that a message board's content is set to auto-expire after a few years in order to protect its participants from getting into trouble over their semi-private conversations. Google and other prominent digital archivists would no doubt comply with the regulation, depriving users of whatever legitimate benefit could be had from searching its content. But there's simply no way to stop, say, a group administrator from burning the archives to disc and then releasing embarrassing posts when another forum denizen runs for office. If data is valued, it will be retained.

I think the proposed system would work decently for preventing employers from going through photos of employees' drunken college exploits, or stopping health insurers from checking clients' web output for hints of preexisting conditions. But it would do very little to affect data retention by individuals — technologically-enforced auto-deletion won't work and encryption makes enforcement nearly impossible. And it's difficult to imagine how a universal technological solution would be any more effective at constraining data retention than simple legislation targeting specific industries that says, "Hey! Throw that data away after X months!"

As a technologist I'm extremely familiar with the temptation to accomplish everything with a well-designed system. But it's very difficult to constrain digital actions with digital technology. Fear of punishment is the only real way to change this behavior — and that can be instilled without rewriting every piece of software in existence.

*Crossposted at* `EchoDitto Labs <http://labs.echoditto.com>`__
