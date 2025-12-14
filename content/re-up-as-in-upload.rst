re-up as in upload
##################
:date: 2008-02-04 17:57
:author: admin
:category: music
:slug: re-up-as-in-upload
:status: published
:save_as: 2008/02/04/re-up-as-in-upload/index.html
:url: 2008/02/04/re-up-as-in-upload/

I won't pretend to be a devoted Clipse fan, but `Spencer <http://toohotfortnr.blogspot.com/2008/02/lift-every-voice-and-sing.html>`__ and `Matt's <http://matthewyglesias.theatlantic.com/archives/2008/02/volume_three.php>`__ excitement over *We Got It For Cheap Vol. 3* has got me intrigued. But I didn't really want to keep my browser open for an hour while I listen to it.

So! Turn on the `Live HTTP Headers <http://livehttpheaders.mozdev.org/>`__ plugin in Firefox. Reload the `streaming page <http://reupgang.blogspot.com/2008/02/re-up-exclusive-we-got-it-for-cheap-vol.html>`__. Capture the conversation between my browser and their server and search for "mp3". What comes up?

   ::

      http://www.mp3asset.com/xml/2008/02/02/7822210.xml?get=1202165719480
      GET /xml/2008/02/02/7822210.xml?get=1202165719480 HTTP/1.1
      Host: www.mp3asset.com
      User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11
      Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
      Accept-Language: en-us,en;q=0.5
      Accept-Encoding: gzip,deflate
      Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
      Keep-Alive: 300
      Connection: keep-alive
      HTTP/1.x 200 OK
      BAR: foo
      Content-Type: application/octet-stream
      Accept-Ranges: bytes
      Content-Length: 286
      Date: Mon, 04 Feb 2008 22:55:28 GMT
      Server: Apache 2.4.0

| What lives at that mysterious
| *http://www.mp3asset.com/xml/2008/02/02/7822210.xml?get=1202165719480* URL? This does:

   ::

      <?xml version="1.0"?>
      <playlist shuffle="0" autoplay="true" color1="231C24" color2="ED2311" color3="984537">
      <sound src="http://www.archive.org/download/Vol.3_734/01Track1_vbr.mp3" stream="true"><![CDATA[We Got It For Cheap Vol.3 Re-Up Gang Records EXCLUSIVE..]]></sound>
      </playlist>

Sure looks like an XML playlist to me. Follow that archive.org URL and what do you get? `The complete downloadable MP3 <http://www.archive.org/download/Vol.3_734/01Track1_vbr.mp3>`__.

Security through obscurity: its track record is at least consistent. Use one-time URLs if you want to keep something semi-private, kids.
