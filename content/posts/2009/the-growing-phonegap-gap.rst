the growing phonegap gap
########################
:date: 2009-04-09 09:52
:author: admin
:category: tech
:slug: the-growing-phonegap-gap
:status: published
:save_as: 2009/04/09/the-growing-phonegap-gap/index.html
:url: 2009/04/09/the-growing-phonegap-gap/

Since the release of WMATA's GTFS dataset I've been reading up on iPhone application development, and in particular the `PhoneGap development framework <http://phonegap.com/>`__. Traditional iPhone development requires a lot of specialized knowledge and the use of Objective C, a language that's used for Apple development and not much else. It takes a significant investment of time to get up to speed.

PhoneGap helps developers sidestep this hassle by providing a ready-to-build iPhone project that moves development tasks into the more popular world of the web. The iPhone app that results is basically a chromeless browser plus some Javascript bindings to iPhone capabilities that a normal webapp couldn't reach — things like GPS, the accelerometer and data storage. Any hack Javascript jockey (hi!) can get an app running using his or her existing skills. The result probably won't be as silky-smooth as a wholly-native app, but it'll be a lot better than a page pulled across the network and into Mobile Safari. And, crucially, it can be listed in the App Store.

Unfortunately, it looks like Apple doesn't like this idea. More and more often the phonegap email list includes cited messages like this:

   | Upon review of your application, [APPLICATION NAME] cannot be posted to the App Store due to the usage of private API. Usage of such non-public API, as outlined in the iPhone SDK Agreement section 3.3.2 is prohibited:
   | "An Application may not itself install or launch other executable code by any means, including without limitation through use of a plug-in architecture, calling other frameworks, other APIs or otherwise. No interpreted code may be downloaded and used in an Application except for code that is interpreted and run by Apple's Published APIs and built-in interpreter(s)."
   | The PhoneGap API implemented in your application is an external framework.

So far the other folks on the mailing list suggest doing a search & replace for the word "phonegap" and then resubmitting the app in the hope that the next reviewer will be less of a stickler.

But these rejections may very well reflect a deliberate policy on Apple's part rather than a mere bureaucratic screw-up. The company consistently introduces roadblocks to development, from their stringent interface guidelines to their nasty habit of charging developers for the privilege of popularizing the company's platforms. Right now, for instance, code and documentation that lets devs experiment with the 3.0 iPhone software — which, among other things, puts Google Maps capabilities in the hands of developers — requires a $99 membership in the Apple Developer program. Worse, that membership often takes an unpredictably long time to be processed — sometimes months.

The intent seems to be to raise the bar on development such that only high-quality software from dedicated, skilled individuals makes its way onto Apple products. It's a a coherent strategy, and certainly in keeping with Apple's position as a premium brand. But it's also a serious drag for developers, diminishes the variety and inflates the pricing of the Apple software universe, and generally imposes yet another cost on Apple users in order to maintain the company's elite reputation.
