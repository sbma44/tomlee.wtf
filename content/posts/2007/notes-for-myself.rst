notes for myself
################
:date: 2007-11-14 16:55
:author: admin
:category: tech
:slug: notes-for-myself
:status: published
:save_as: 2007/11/14/notes-for-myself/index.html
:url: 2007/11/14/notes-for-myself/

NBC Direct's DRM may be a tougher nut to crack, not least of all because of its insistence on using IE on XP. I don't have an XP machine, and IE precludes the reliable mix of Firefox plugins that makes pulling apart website behavior a breeze. You can accomplish the same thing with other tools, but it's a much bigger pain in the ass.

At any rate, here's the XML that a properly authenticated request will return. As you can see, there's not much useful here — I was hoping for a URL or encrypted key, but no such luck. Sniffing the HTTP traffic of the following exchange is the next thing to do. Given the XPcentricity of the app, I'm optimistic that `this stuff <http://forum.doom9.org/showthread.php?t=127943>`__ would work on the downloaded files.

   ::


      <!--
      returned by command
      curl -A"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)" "http://www.nbc.com/app/direct/services/?method=provisionLicenseAndDownload&assetPk=200135&devicePk=220499&productPk=200027"
      -->
      <?xml version="1.0" encoding="UTF-8"?>
      <DirectProductGuide>
      <provisionLicenseAndDownload>
      <key_0>
      <accountFk>221752</accountFk>
      <assetFk>200135</assetFk>
      <completeDate></completeDate>
      <completeNote>Register asset message queued for S200122D200158E200159T200160C200161</completeNote>
      <deviceFk>220499</deviceFk>
      <productFk>200027</productFk>
      <profileFk></profileFk>
      <provisionId></provisionId>
      <provisionName>30 Rock | Greenzo</provisionName>
      <provisionPk>271150</provisionPk>
      <provisionStatus>scheduled</provisionStatus>
      <provisionType>download</provisionType>
      <purchaseFk></purchaseFk>
      <requestDate>2007-11-14T21:41:42.716Z</requestDate>
      <xmlData></xmlData>
      </key_0>
      <key_1>
      <accountFk>221752</accountFk>
      <assetFk>200135</assetFk>
      <completeDate></completeDate>
      <completeNote>License new message queued for S200122D200158E200159T200160C200161</completeNote>
      <deviceFk>220499</deviceFk>
      <productFk>200027</productFk>
      <profileFk></profileFk>
      <provisionId></provisionId>
      <provisionName>30 Rock | Greenzo</provisionName>
      <provisionPk>271151</provisionPk>
      <provisionStatus>initiated</provisionStatus>
      <provisionType>license</provisionType>
      <purchaseFk></purchaseFk>
      <requestDate>2007-11-14T21:41:42.822Z</requestDate>
      <xmlData></xmlData>
      </key_1>
      <status>success</status>
      </provisionLicenseAndDownload>
      </DirectProductGuide>

It's all just an academic exercise, of course — all this stuff is `on Bittorrent already <http://isohunt.com/torrents/?ihq=30+rock+s02e05>`__.
