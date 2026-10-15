---
title: My Summer of Slop
date: 2026-10-15
author: admin
category: Uncategorized
slug: slop
status: published
---

I should admit now that I'm not much of a basketball fan, and perhaps that's my problem. I see the appeal, of course. Superhuman athleticism. Knowable numbers of outsize personalities. Seamless integration with the vanguard of pop culture cool. A burnished, heroic aesthetic perfected through the application of countless Nike ad dollars. Global and cosmopolitan, and yet also an enduring symbol of American achievement. It's undeniable.

And yet I have trouble sitting through the games. _The Success Equation_ popularized the notion of a skill/luck continuum, characterizing sports by their number of scoring chances and noting that basketball skews toward the low-luck end of the spectrum: the teams that win really are reliably the best. That's admirable, I guess, but I find it a bit unexciting in practice. Combined with tanking, star player rest days, the relative reliability of talent scouting, and the dreariness of games' final minutes being made up of free throws--to me, it's a wasted opportunity, and leaves me reluctantly opting for anonymously helmeted football players or uncharismatic (but excitingly violent) French Canadians when I'm picking what sport to watch.

But I am a Washingtonian, and my friends are avid Wizards fans. The team has been in the news thanks to its number one draft pick. I find the hapless Wizards amusing and endearing, and I will shamelessly jump on the next bandwagon that presents itself. I also find [the deadpan combination of pro basketball and the occult](/2022/10/31/the-house-of-endless-mourning-feat-the-harlem-globetrotters/) to be profoundly funny and, despite being unable to fully explain why, I have already devoted many, many hours to riffing on the theme.

It's particularly funny for the Wizards given the circumstances of their name. Shamed by D.C. gun violence, the team announced a name change and picked "Wizards" from among a set of even-worse possibilities. They seem to have regretted it almost immediately, and have embraced the absolute minimum amount of wizard iconography possible. I think this is a shame. I love wizards, and I know a lot about them.

These observations weren't new to me, but their formulation as a project was: an NBA arena-ready hype track that imagines the Wizards embracing their thematic pedigree as intensely as possible. It was the very start of summer--I remember, because ideas for verses were running through my head the whole time I was with my family at our end-of-school trip to the beach. _What mystical terms rhyme with "Coulibaly"_, I pondered as I watched my children board a rollercoaster.

By the time we got home I was pretty satisfied with what I had in my phone's notes app. This is the point where the siren song of slop enraptured me.

Let me say this now, clearly: I regret nothing. I worked hard on this project, and I learned a lot. I will recount all of that here at potentially tedious length. I remain amused and even proud of what I produced.

It is clear, though, that essentially everyone else hates it. I should have been more open to this possibility, I suppose, and I am still teasing out the full array of reasons why it is so unwelcome. But I find this revelation doesn't bother me much. And I feel that belated understanding, even if partial, is better than none.

## Audio Slop
Up to this point, the project was entirely human. Sure, I tried passing what I had over to AI for suggestions, but what came back was quite bad. Other than suggesting a couple of wizard-related franchises that I'd forgotten about, AI contributed nothing to the jokes in the video.

My next stop was Suno, a service that creates generative AI music. I knew that people held the results in low esteem, but that was fine: I wanted something shlocky, that was part of the joke. Some iteration on the prompt--Suno steadfastly refused to acknowledge specific artists I entered, doubtless for IP reasons, but summarized their genres--and I got a track out. It wasn't quite right, and I attempted endless tweaks, adding bracketed instruction amid the lyrics where I wanted a pause or a change in vocalist. But it was extraordinarily hard to control the results. The exercise felt more like a slot machine than anything else. Still, with enough pulls of the lever, I finally got back something I liked.

The lyrics had been my planned stopping point. Then the Suno track became my planned stopping point. But I asked Claude what it would take--just hypothetically!--to start making a video to accompany it.

Months later I had learned Final Cut Pro, constructed multiple CGI sequences in Blender using a small render farm, and edited together over 126 short shots, timing them with millisecond precision. You can find the result on Youtube if you search for "Wizmarillion".

## Video Slop
I started in iMovie--it's free, after all. But it was frustrating to keep clips pinned to specific moments of audio, and you can rent Final Cut on a monthly basis these days. That switch came early.

I didn't construct a storyboard or some other grand plan--didn't seem fun, and I didn't have enough ideas to fill the timeline. I just focused on a verse or two at a time, starting on whatever remained that I found most amusing, slowly dragging myself across four minutes of content a few seconds at a time. By the time I wrapped up (with a last burst of energy for the post-credit sequence), I was quite ready to be done. The dragon/Metro sequence still looks awful to me, but I couldn't be bothered to fix it. I'm grateful to the loyal friend who reliably faked enthusiasm for this project as I shamelessly used texts to him as a commitment mechanism. It was much, much more work than I expected--though also the kind of work that can be done in 5 second bursts during a conference call, or with an episode of _Reacher_ on in the background.

The core workflow occurred in LTX Studio, a web-based wrapper around a variety of image and video models. There are other sites very much like it. LTX distinguishes itself by letting you create "elements", reusable figures or objects that are characterized by a series of reference images you upload. This allows for scene-to-scene consistency.

How to get those images? With a static image model. Google's Nano Banana Pro, ChatGPT's image model, and Midjourney seem to be the big players here. I mostly used Nano Banana. For all of them, you can upload one or more reference images plus a text prompt that explains what you want it to do. You can omit the image entirely and have it start from scratch. But it's often productive to have a starting point.

There are filters in place that are applied to the text prompt, which enforce various policies designed to prevent misuse. But these are easy to defeat. A typical workflow--say, to put Alex Sarr in flowing wizard robes and create an LTX element--would start with a bunch of Google Image Search results pasted into LTX, with Nano Banana selected. My prompt would refer to him as a basketball player--not one with a specific name or team affiliation, mind you. I'd ask it to adjust his wardrobe, give him a beard, make his hat pointier, add some stars. Remove the background, make it a neutral color. Give me a headshot. Reference shot, neutral lighting. Turn him in profile. Great. We define the element, then start using it to make content.

LTX has its own relatively cheap video model, plus access to more expensive models like Seedance, Kling, and Google's Veo. They all have their quirks, and they're all quite stupid. Asking one of the still image models to start from scratch can deliver interesting results. It's usually unwise to try this with a video model. More typically you upload a starting frame that you've created with a still image model. Optionally, you add an end frame. You specify the resolution and length of the clip you want--never more than a few seconds (I often found myself discarding content as I pared down from the minimum of 2 or 3 seconds). And you provide a text prompt explaining what happens over the course of that clip.

(There are modes that let you add video as a starting point, rather than images, to replicate input movement with entirely different ornamentation. Also audio, for lip syncing. These worked very poorly for me and I barely used them, but you've probably seen video where people managed better results than I did.)

Writing the video prompt is tricky. The models create output that stretches over time, of course, but they do not understand causation. You must write as if everything is happening at once, counting on your words constraining the model toward favoring the narrative output you envision. You spend a lot of time scolding the model. _Do NOT create additional basketballs, there should NEVER be more than one basketball during the ENTIRE duration. The lighting is STEADY throughout the clip, EXTREME consistency. Extremely slow, gentle dolly in, the camera moves in a single direction at a continuous clip throughout, NO abrupt moves or zooms_. It's very tedious and I had Claude write a lot of these.

The more expensive models are better, but each model is idiosyncratic. It's clear that Veo has watched some sports; LTX's homegrown model has not. None of them know how many panels are supposed to be on a basketball. None of them understand how to draw a unibrow over a third eye. The LTX model badly wants to do dramatic speed ramping at the beginning and end of clips. None can handle dramatic camera movements or lots of figures moving in complex ways. I had to ask Claude to build Blender sequences like the D20 flying into a basket (still my favorite shot in the video). The technology does not yet exist to make a roomful of G-Man mascots replicate a NHPC step routine, which I realize many readers will consider to be a blessing.

Encountering these limitations made me adjust my plans and abandon certain ideas I thought would be funny (I didn't bother to attempt to depict a no-look pass through a Doctor Strange-style portal). It also taught me a lot about the relative sophistication of different AI video creators--perhaps the least-desired critical skill imaginable, I know. Next time you see a Gossip Goblin clip, count how many shots move the camera or include more than two or three (admittedly strikingly grotesque) figures talking to one another. Constraints are necessary for art, sure, but right now these tools are not just constraining but constricting.

In a way this gave me more respect for their use. The results are usually without any artistic merit, I know. But there is nonetheless a particular kind of effort and skill involved. Naturally, it's nothing compared to practitioners of the types of art they're aping. I think that's okay, though, as long as we don't get confused and imagine the two are the same kind of thing.

I rationalize this project, in part, by its impossibility in the absence of the tools. I'm amused to have created something complete and coherent which could never be justified if it required conventional forms of production. Many would say that impossibility is for the best, I know.

But I found there to be something liberating about what I was newly empowered to do. I cannot perform hip-hop or run a complex video production, nor justify spending money on experts who could do those things for me--certainly not for something this stupid. But I can write lyrics and jokes and do some video editing, and it's exciting to be able to fill in the gaps in my capacities toward a creative goal without needing to find collaborators or budget that don't exist.

## The Nature of Slop
My favorite definition of AI slop is content that takes more time to consume than it does to produce. By that standard, I can assure you that this project does not qualify. Every cut you see is manual, and endlessly fussed over; every shot is the result of dozens of prompts and revisions.

In other senses, though, this is obviously slop. The appropriation of others' likenesses for jokes-by-reference is the most obvious characteristic. It's a lazy kind of humor, but one I didn't bother resisting since invoking cultural references--albeit a specific subset of them--is the effort's fundamental gag. There is nothing truly original here: various nerdcore artists have been mining the dissonance between hip-hop culture and geek obsessions for laughs for at least twenty years. I can admit this while still feeling pride in the "came up hard / Isengard" couplet.

I went to some lengths to keep the video at a legally plausible remove. Those preparations now seem quite silly: to the extent anyone cares, I think they intensely dislike what I made. Virtually every relevant subreddit bans AI content, presumably having been flooded with it during eras where I wasn't yet paying attention. I did get a nice note from someone on an AI video subreddit, but it soon became apparent he was just promoting his Discord project. Otherwise: crickets and downvotes, a couple dozen views on Youtube.

The reasons aren't particularly hard to fathom. A lot of the internet has been polarized against AI. I think this attitude is a little hyperbolic and insular, but not wildly so. Stigmatizing AI's use in creative fields strikes me as a good and probably necessary idea, even if I wish hobbyist efforts as silly and noncommercial as mine could get a pass.

Beyond that, I suspect sports fans prefer to assume a kind of masculine dignity that my project is not eager to grant them. The number of people who feel affection for both dungeons & dragons and the NBA is growing but small. The people who care about the Washington Wizards is also small, and they probably don't appreciate my mean-spirited digs at Gilbert Arenas and Ernie Grunfeld (both of whom have been gone from the franchise for many, many years) or the caricatures I made of their current crop of rising stars.

Despite this, I'm proud to have finished something big. And I still smile when I press play. That last bit is the only part that I genuinely feel embarrassed about.