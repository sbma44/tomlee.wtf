---
title: Govtech in the Era of Claude Code
date: 2025-12-29
author: admin
category: Uncategorized
slug: govtech-in-the-era-of-claude-code
status: published
save_as: 2025/12/29/govtech-in-the-era-of-claude-code/index.html
url: 2025/12/29/govtech-in-the-era-of-claude-code/
---
Andrej Karpathy notes that ["people who aren’t keeping up even over the last 30 days already have a deprecated world view" about using LLMs to write code](https://x.com/karpathy/status/2004621825180139522) and that [devs must "rapidly progress through their grief cycle"](http://x.com/karpathy/status/2004974725320347884) to find their new place in the profession. I think he's right. I haven't written software professionally except in a glancing way for a long time, but I've felt myself gain what feel like enormous new powers and [watched others achieve truly towering things](https://friendlybit.com/python/writing-justhtml-with-coding-agents/).

Things are moving faster than even those at the field's forefront can figure out. But I don't think it's too early to begin thinking about what this might mean for how government builds technology.

## Old problems and their old solutions
The cause of government's inability to build excellent software has been diagnosed in various ways at various times.

In the early civic tech era, we felt government didn't realize what was achievable. This was true at the time, but--at least until AI arrived--had ceased to be a serious problem.

Government's inability to manage complex software projects implemented by third parties was next, chalked up to some mix of procurement rules, monolithic design practices, and a lack of institutional expertise. This remains a serious problem but great progress has been made through the evangelism of agile methodologies, the creation of digital services teams, procurement thought leadership, and creative approaches to attracting (and compensating) software talent.

Then DOGE arrived, and blew it all up. I had been wondering how it will be rebuilt. Perhaps some kinds of civil service reform that make it easier to hire, fire, and pay people? A disaggregation of the 18F/USDS offices toward DS teams in less central locations (a trend already underway)?

I think those things are still likely, but it is becoming clear that the next era will be built in a world where software engineering, as a discipline, has dramatically changed. I'm not sure what that will mean, but I can think of at least four likely trends.

## Fewer, but better
First, in-house expertise will be more important than ever. The amount of production codebase that a single software architect can deliver has gotten dramatically larger, and has not yet stopped expanding. There are inevitably layers between an agency's requirements, as embodied by its statutory obligations, political imperatives, and institutional knowledge, and a deployed application. But those layers are going to become very thin, very fast. This will make exciting new things possible, but it will also mean that the people who embody them will have less redundancy. Stupid mistakes will become easier; the premium to smartness will increase.

## Cybersecurity as subdiscipline instead of compliance function
The level of human understanding of deployed codebases is plummeting. People will complain bitterly about this on Bluesky, but it's inevitable. Many of the negative consequences of this can be ameliorated by instilling good, traditional development practices into our new tools and the procedures that surround them--tell your .cursorrules to write lots of tests; run beta periods with humans and agents; do perf testing and, way before that, nail down your architecture while someone who understands the relevant issues is behind the steering wheel.

Still, there's inevitably going to be more dark matter. Cybersecurity expertise will be important for understanding the landscape of risk and prioritization. Pointing Claude at a NIST checklist is not going to cut it.

## Which agency do you think Garry means?
![tweet from garry tan: "intelligence is on tap now so agency is even more important"](/static/2025/12/garrytan.png)

When he says [this](https://x.com/garrytan/status/1894063324582625732)? Kidding, of course. (And heck, it seems like "agency" as a buzzword is [already going out of fashion](https://x.com/tszzl/status/2005042727172669637).)

Still: when you use these tools, the importance of having ideas and executing them to completion does inevitably present itself as the thread we must cling to as this technology strips away our pride in other human talents. It's a tendency we'll all have to cultivate more intensively, certainly including myself.

In the case of government, though, there are some novel kinds of hindrance. Feds cannot "just do things". We can all recite at least some of the litany of well-meaning rules that grind government to a halt. The FAR. Hiring rules. The PRA. The other PRA. The list goes on.

[Brilliant people are already working on this](https://www.recodingamerica.us/), but the pressure is going to increase as agencies' expanded productive capacity makes them feel stymied even more often and, perhaps, begins to overwhelm some of the people manning the barricades. At the same time, DOGE's catastrophic legacy of failure will chasten any thought of radical reform. I have no idea how this will shake out, but it's going to be intense.

## Programming will definitely get cheap. Programmers might, too.
We've all learned about Jevons' Paradox, sure. But I am not so sanguine about what the labor market for programmers will look like at the start of the next presidential administration. Only a fool would guess at the state of the economy that far in the future, but I will not be at all surprised if the famed stability of a government job--whether that promise is still true or not--begins to attract more talented technologists for a given federal salary. That could, in part, be because their private sector compensation prospects have fallen.

There's an even darker version of this story: government could become *the* anti-AI refuge for workers, a safe haven from accelerating efficiency. This seems particularly easy to imagine if the Democratic Party allows itself to become negatively polarized into the anti-AI party, as countless left-aligned posters spinning threads about water use and copyright are pushing. It will not be easy for the party's leadership--aged, hated, repudiated--to seize the mantle of responsible governance of this bewildering new technology, rather than succumb to populist antimodernity.

I say all of this with a sense of melancholy about what we're about to lose. But there is no sense denying the inevitable: soon, many kinds of tasks will no longer be performed by humans outside of classrooms. And this seems likely to apply to software more than most fields. That's at least a little sad for those of us who are entranced by computers.

But it will also come with benefits. And not least of these could be government getting dramatically better at serving its citizens. Before long we could all have a pretty-good caseworker assigned to each of us for every otherwise-bewildering bureaucratic maze that was designed for a markup session rather than human clients. Tax filing, benefit applications, financial planning, program eligibility--an infinitely patient social worker whenever anyone needs one. Believe me, I can imagine exactly how this paragraph would get roasted on Bluesky. But there are people who need this kind of help and aren't getting it, and (yes, I see the reply you were drafting) _won't_ get it without a breakthrough this epochal.

Heck, in some ways government might even enjoy a relative procedural advantage: everyone else's talent pipeline is now hopelessly clogged with garbage submissions designed to game the system. But the feds have been laboring under those conditions for decades! Throwing a few AI resumes on the pile probably won't slow them down much.

## These are good guesses today
But they'll probably be wrong soon. It feels a little paradoxical to say that things are moving so fast that, for now, all we can do is watch and wait. But I think it's approximately true. We have to at least wait to hear the sonic boom. In the meantime I intend to keep using and maybe even understanding these new tools.