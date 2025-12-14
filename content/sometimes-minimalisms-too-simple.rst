sometimes minimalism's too simple
#################################
:date: 2011-02-01 12:30
:author: admin
:category: Uncategorized
:slug: sometimes-minimalisms-too-simple
:status: published
:save_as: 2011/02/01/sometimes-minimalisms-too-simple/index.html
:url: 2011/02/01/sometimes-minimalisms-too-simple/

Like `Ezra <http://voices.washingtonpost.com/ezra-klein/2011/02/that_is_what_it_does.html>`__, I find `this explanation <http://delong.typepad.com/sdj/2011/01/dropbox-on-quora.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed:+BradDelongsSemi-dailyJournal+(Brad+DeLong's+Semi-Daily+Journal)>`__ for Dropbox's success intellectually attractive.  Minimalism!  Of course!  It's so simple!  It's exactly the kind of thing that software developers get off on. For one thing, it legitimizes our lust for Apple products -- despite the fact that Apple UI betrays the idea more often than we admit -- because most of us can't or don't want to distinguish between *good aesthetics* and *simplicity*.  It's sort of zen.  It makes us feel wise.  But in this case I don't buy it.

Here's what I think happened.  Amazon launched its `S3 service <https://s3.amazonaws.com/>`__.  Suddenly you could buy Big Storage services at essentially marginal cost, immediately.  No physical capital expenses, and human capital expenses were dramatically reduced (now you need a programmer who can work with AWS, but not someone who can source, install and manage huge RAID arrays in a datacenter somewhere).

That happened, and then a bunch of people tried to resell this service with some paper-thin rebranding/UI work.  Kevin Rose and Leah Culver with Pownce, and some Flickr clone with too many O's in its name, and whatever, a bunch of people.  Dropbox was the first -- as far as I know -- to come up with a funded business model that could provide a useful amount of synced storage for free.

Also -- and this is something that the Quora answer completely underplays --  Dropbox is quite technically sophisticated.  It's not just rsync on a minute cron, you know.  It's hooking into filesystem interrupts to notice when stuff changes in the synced folder, and doing it natively on every major OS.  It's got quiet but powerful ways of dealing with versioning conflicts.  It's also doing all of this with a high degree of polish (I mean: Growl notifications, c'mon).  Plus it's smart enough to do things like notice when it needs to sync within a LAN instead of over the net, avoiding complexities you might not have considered like NAT traversal.  It's not that it's so simple; it's actually a very sophisticated execution.  It's just that those parts aren't necessarily visible (and no, many of its competitors were not as clever).

Now, this is minimalism, in a sense.  But it's not the sort of minimalism pointed to in the Quora answer, which amounts to "Let's offer fewer features than those other jerks and we'll all get rich!"  It's more about doing things that are sophisticated and difficult, and not wasting time on UI afterthoughts.

It was 2006 when S3 launched, but a few years isn't THAT long for a specialized market to shake out.  Besides, S3 prices have been falling since its launch, so it could've either been a lack of investment in the synced-storage space or just the need to wait for a cheaper equilibrium point that delayed the rise of a winner in the space.  At some point a critical mass was reached and brand recognition took over.

Anyway, Amazon's contribution to web infrastructure is the key here.  Its transformative field-leveling effect on the industry (and the web's increasing reliance on it) is a story that ought to be explored more in the popular press.  AWS deserves a bit more of the concern that Google commonly attracts for its market power.
