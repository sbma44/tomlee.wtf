good reasons for thinking crypto is bad
#######################################
:date: 2021-11-23 15:54
:author: admin
:category: Uncategorized
:slug: good-reasons-for-thinking-crypto-is-bad
:status: published
:save_as: 2021/11/23/good-reasons-for-thinking-crypto-is-bad/index.html
:url: 2021/11/23/good-reasons-for-thinking-crypto-is-bad/

By citing one of my tweets, Will Wilkinson has done me the immense favor of inviting me to an internet argument I can join without getting in trouble. I am embarrassed at the genuine thrill I felt at this. My wife has been asking what she should get me for Christmas, and I've been hemming and hawing about various electronic gadgets in response. But now it's clear what I really want to find under the tree: trackbacks.

`Will's been writing about cryptocurrency <https://modelcitizen.substack.com/p/is-crypto-bullshit>`__--aka crypto, as it's annoyingly abbreviated, aka web3, which is more annoying still. He notes this annoyance and is right, of course, that it exists, is widespread, and cannot be counted as an argument.

So let me gin up some arguments. But first, I'll offer my bona fides, which consist almost exclusively of making serious mistakes about this subject:

- I lost--or rather, am on the cusp of losing, pending Japanese regulators finalizing the paperwork--more than $80k USD in Bitcoin thanks to the MtGox bankruptcy (this was a $400 initial investment).
- My high school friend Victor made a substantial early investment in crypto assets, which I begged him to sell or at least differentiate. He ignored me, bought a larger house, retired before 40, and now travels the world.
- I accepted $20 in Bitcoin payment from my friend `Eric <https://twitter.com/konklone>`__ for supplies associated with `an Arduino class I taught </2014/06/30/arduino-class-notes/>`__, which subsequently ballooned to an amount so large I am too embarrassed to bring it up with him.
- I lost a hundred dollars in Dogecoin during that fun Elon Musk SNL news cycle. Remember that?
- I currently have about $8k in Coinbase which I flip between Ethereum and cash, nearly always mistiming the trade yet still gaining value thanks to how mulishly bullish the market is.
- I have read the Solidity docs and some tutorials, which were confusing and then boring.
- I have installed mining software after buying a fancy video card, but always turned it off when I needed my GPU for something more serious (e.g. Overwatch, which I am also bad at).
- I have read almost everything `Tim Lee <https://fullstackeconomics.com/>`__ has written about cryptocurrency over many, many years (this one is not a mistake).

So I've been crypto-adjacent. Close enough that I agree with Will: there is some there there.

Fundamentally, there is beauty. Anyone with even a little understanding of computer science must look upon Satoshi's innovation with awe. It's an intellectual marvel, something that should have been impossible but which works. Ditto the Ethereum blockchain, which adds a programmable layer of abstraction atop that first fundamental insight. I'm sure there are other masterpieces of genius scattered through the field, too, though I haven't gone hunting for them; and they seem increasingly likely to take the form of financial innovation rather than CS. Nevertheless: it is the beauty of the underlying ideas that got a lot of technical people excited in the first place, and which continues to power much of their zeal.

But what is that idea? I'll try not to write yet another explainer. I'd do a bad job, anyway. But basically: security without trust. Transactions without a central authority. A way to assign everyone so much math homework that they don't have time to cheat you. They can't falsely claim to have assets they don't, or fail to hold up their side of a bargain. It's impossible, for reasons that are so weird and elegant as to be nearly ineffable.

It's important to emphasize that this is the system's only advantage. A lot of overhead comes with that math homework. With a central, trusted authority you can do all of the same things, do them faster and with fewer resources, and do them in a way that allows mistakes to be corrected.

Centralization is so great, in fact, that the cryptocurrency community hasn't been able to resist embracing it. It's been years since it was economical to mine outside of a pool, where effort and rewards are shared. And the lure of subsidized electricity was so strong that, prior to a recent nationwide crackdown, the `predominance of Chinese miners put the entire Bitcoin blockchain at risk <https://news.bitcoin.com/chinese-mining-threatens-bitcoin/>`__ (if 51% of the ecosystem's participants coordinate an attack, all the aforementioned promises of trustless security fail).

Blockchains' technical guarantees being subverted by governance isn't theoretical. Famously, `Ethereum hard-forked the system after some hackers stole a bunch of people's money <https://en.wikipedia.org/wiki/The_DAO_(organization)#:~:text=In%20June%202016%2C%20users%20exploited,funds%20to%20the%20original%20contract.>`__ using a design flaw in a system built atop their chain (there was no underlying problem with Ethereum). This wasn't possible under the rules of the system as they're usually presented. It happened because the project had respected, centralized leadership and its participants very strongly wanted an exception to be made. The Bitcoin devs' monarchical reign over critical system design elements like block size echoes this sense (harder to shake the older I get) that every immutable rule we declare is built out of simian hierarchy and inertia.

Another centralizing phenomenon: the fact that a large amount of cryptocurrency trading occurs "off chain". Running transactions that affect the blockchain is expensive and slow--problematically so, in the case of some chains, including Bitcoin. So there are "lightning nodes" that settle transactions internally, then periodically update the chain with the result. Similarly, exchanges like Coinbase provide instant trading by swapping values around in their own, off-chain systems--they process enough transactions to make this viable--and periodically reconciling their accounts with the blockchain.

This is all perfectly normal--it's how stock brokerages work, too--but in my experience it's usually not included in the triumphalists' elevator pitch.

I admit: it is still possible to avoid at least some of this centralizing tendency. There are plenty of virtually rich weirdos with their wealth encoded in idiosyncratic forms that they control utterly. Even in a world of steadily expanding KYC rules, it's possible to become a crypto gazillionaire while remaining anonymous. It's possible to spend some of it by using shady offshore coin mixers or whatever system has supplanted them since I last paid attention. There are dudes on Craigslist who will meet up with you in a park and sell you a slip of hexadecimal numbers. All that wildcat stuff still exists.

But one suspects that's not `how Morgan Stanley is doing it <https://markets.businessinsider.com/news/currencies/13-top-banks-investing-cryptocurrency-blockchain-technology-funding-blockdata-bitcoin-2021-8>`__. `Nor the recently-debuted Bitcoin ETFs <https://www.kiplinger.com/investing/cryptocurrency/603600/bitcoin-etfs-cryptocurrency-funds>`__. These pools of wealth will keep growing. They'll have an advantage relative to on-chain transactions that increases with their size, even apart from the sociocultural advantages that come with institutional scale and prestige. It seems likely to me that they'll eventually be absorbed into our existing, deeply regulated financial infrastructure.

There are technical schemes and alternative blockchains designed to combat all of this. It'll surely be a long time before you can no longer keep the cryptographic equivalent of a pile of cash under your mattress. But I think the centralizing tendency is real and more or less inevitable, particularly when combined with the undeniability of the early chains' first mover advantage.

As I pointed out in the tweet Will quoted: this is consonant with governments' wishes. Suffering an untouchable deflationary monetary system is no hegemon's idea of a good time. Some, like China, will lash out. Wiser leaders will wait patiently for these systems' share of wealth to swell within their own borders, and then watch them trickle through national financial watersheds and into reservoirs controlled by people who are on reelection committees.

This is a longwinded way of saying: I think the promise of crypto will prove to be a sham. Operating without a trusted authority is harder and less desirable than it sounds. This is also why I'm not too worried about the environmental case against it. After centralization, the problem will be tractable. Mining gets steadily *\*less\** lucrative, you know. You don't have to obsessively refresh pages on newegg.com to charge someone a management fee.

There are some loose ends to tie up:

- Will mentions a number of projects that use crypto primitives in novel ways. Helium, Filecoin, Render (which I hadn't heard of, but sounds cool). I am pretty excited about some of these (note that Helium is a customer of my employer). In some cases the blockchain stuff may just be window dressing--a clever way to generate a more elastic response to a vanilla subsidy as an actually-centralized project bootstraps its growth. But if their goal is useful, whatever, good for them.
- NFTs are bad. The art is bad, `the scene is bad <https://www.inputmag.com/culture/bored-ape-yacht-club-nft-nyc-ape-fest>`__, but it's really the ideology that's the pits. The promise of abundance is why I love digital technology. It's liberatory, a genuine miracle. To find ways to reinvent scarcity in the absence of material need--primarily to fuel a status competition that doesn't even offer an epicurean or cultural rationale but is genuinely *only* about displaying wealth--it would be hard to imagine a more pathetic moral surrender. Just despicable, top to bottom.

After all that, what is left? Getting rich, of course! It's a bull market--you still have to be a real idiot to lose money on crypto these days (see above). And it's a greenfield. The kind of place where smart people can plausibly create generational wealth by seeing something others don't.

I often think of *Fortune's Formula*. It's a fun book. Formally, it's about a statistical insight related to wagering in financial settings that made people rich. But I think it's more important as a history. Clever young men from Bell Labs; from Las Vegas; from the mafia. Ones with assiduousness and the ability to see new opportunities in old flows of money. They start out counting cards and end up inventing the hedge fund industry. Many become incredibly wealthy.

It's a fascinating story, and I read it intently. What did those men accomplish along the way? I couldn't tell you. That wasn't the point.
