are dc's speed cameras racist?
##############################
:date: 2024-04-12 14:42
:author: admin
:category: Uncategorized
:slug: are-dcs-traffic-cameras-racist
:status: published
:save_as: 2024/04/12/are-dcs-traffic-cameras-racist/index.html
:url: 2024/04/12/are-dcs-traffic-cameras-racist/

*This is the first of my posts about speed cameras.* `Part 2 is here </2024/04/13/traffic-cameras-extended-edition/>`__\ *\ .* `Part 3 is here </2024/04/19/speed-cameras-legacy/>`__\ *.*

The two most important things about speed cameras are that they save lives and that they are annoying. People think life-saving is good. They also think getting tickets is bad. These two beliefs are dissonant. Social psychology tells us that people will naturally seek to reconcile dissonant beliefs.

There are lots of ways to do this, some easier than others. For speed cameras, it typically means constructing a rationale for why *cameras don't really save lives* or why *life-saving initiatives aren't admirable.* A common approach is to claim that municipalities are motivated by ticket revenue, not safety, when implementing automated traffic enforcement (ATE). This implies that cameras' safety benefits might be overstated, and that ATE proponents are behaving selfishly. Most people understand that this is transparently self-serving bullshit. It's not really interesting enough to write about.

But there's another dissonance-resolving strategy that popped into my feed recently that merits a response: *what if speed cameras are racist?*

This strategy doesn't attempt to dismiss the safety rationale. Instead, it subordinates it. *Sure, this intervention might save lives*, the thinking goes, *but it is immoral and other (unspecified, unimplemented) approaches to life-saving ought to be preferred.*

This argument got some `fresh life <https://twitter.com/samswey/status/1770122530873098679?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1770122530873098679%7Ctwgr%5E7126f9ff618fac7c5c91f5987da40999ba4aad3a%7Ctwcon%5Es1_c10&ref_url=https%3A%2F%2Ftomlee.wtf%2Fwp-admin%2Fpost.php%3Fpost%3D3509action%3Dedit>`__ recently, citing `a DC Policy Center study <https://www.dcpolicycenter.org/publications/predominately-black-neighborhoods-in-d-c-bear-the-brunt-of-automated-traffic-enforcement/>`__ that makes the case using data from my own backyard.

.. container:: float wp-block-image aligncenter size-large

   |image1|

I appreciate the work that the DC Policy Center does. Full disclosure: I've even cited this study approvingly in the past (albeit on a limited basis). But this tweet makes me worry that their work is transmuting into a factoid that is used to delegitimize ATE. I think that would be unfortunate.

So let's look at this more closely. We can understand the study and its limitations. And, because DC publishes very detailed traffic citation data, we can examine the question of camera placement and citation issuance for ourselves--including from an equity perspective--and come to an understanding of what's actually going on.

What does the DCPC study SHOW?
------------------------------

The most important result from the study is shown below:

.. container:: float wp-block-image size-full

   |image2|

The study reaches this conclusion by binning citation data into Census tracts, then binning those tracts into five buckets by their Black population percentage, and looking at the totals.

Descriptively, the claim is correct. The Blackest parts of DC appear to be getting outsize fines. But the "60-80% white" column is also a clear outlier, and there's no theory offered for why racism--which is not explicitly suggested by the study, but which is being inferred by its audience--would result in that pattern.

To the study's credit, it acknowledges that the overall effect is driven by a small number of outlier Census tracts. Here's how they discuss it at the study's main link:

   Further inspection reveals five outlier tracts which warrant closer inspection. Four of these outliers were found in 80-100 percent black tracts while one was found in a 60-80 percent white tract. Of course, by removing these extreme values, the remaining numbers in each racial category do fall much closer to the average. But notably, the number of citations and total fines per resident within black-segregated tracts remains 29 percent and 19 percent higher than the citywide average, even after removing the outlier locations. Meanwhile, the considerably lower numbers of citations and fines within 80-100 percent white census tracts remain considerably lower than average. **(For a more in-depth discussion of the results and the effect of these outliers, please see **\ `the accompanying methods post on the D.C. Policy Center’s Data Blog <https://dc-policy-center.github.io/posts/automated-traffic-enforcement>`__\ **.)**

But if you click through to that "methods post" you'll find this table, which has been calculated without those outlier tracts. The language quoted above isn't inaccurate. But it's also clearly trying to conceal the truth that, with those outliers removed, the study's impressive effect disappears.

.. container:: float wp-block-image aligncenter size-full

   |image3|

What do we know about DC's ATE cameras?
---------------------------------------

Let's take a step back and look at this less reactively. What do we know about DC speed cameras?

The most useful source of data on the topic is DC's moving violation citation data. It's published on a monthly basis. You can find a typical month, including a description of the included data fields, `here <https://opendata.dc.gov/datasets/DCGIS::moving-violations-issued-in-january-2022/about>`__. I had previously loaded data spanning from January 2019 to April 2023 into a PostGIS instance when working on `this post </2023/02/03/fake-tags-are-a-real-problem/>`__, so that's the period upon which the following analysis is based.

The first important signal we have to work with is the *issuing agency.* When we bin citations in this way, we see two huge outliers:

.. container:: float wp-block-image aligncenter size-full

   |image4|

ROC North and Special Ops/Traffic are enormous outliers by volume. We can be sure that these represent speed cameras by looking at *violation_process_desc* for these agencies' citations: they're all for violations related to speeding, incomplete stops, and running red lights. The stuff that ATE cameras in DC detect, in other words.

I am primarily interested in ATE's effect on safety. The relationship between speeding and safety is very well established. The relationship between safety, red light running and stop sign violations is less well-studied. So I confined my analysis to the most clear-cut and voluminous citation codes, which account for 86% of the citations in the dataset:

::

    violation_code |          violation_process_desc          
   ----------------+------------------------------------------
    T118           | SPEED UP TO TEN MPH OVER THE SPEED LIMIT
    T119           | SPEED 11-15 MPH OVER THE SPEED LIMIT
    T120           | SPEED 16-20 MPH OVER THE SPEED LIMIT
    T121           | SPEED 21-25 MPH OVER THE SPEED LIMIT
    T122           | SPEED 26-30 MPH OVER THE SPEED LIMIT

I'm not going to focus on human speed enforcement, but it is interesting to examine its breakdown by agency:

.. container:: float wp-block-image aligncenter size-full

   |image5|

`DC publishes the location of its ATE cameras <https://ddot.dc.gov/publication/automated-traffic-enforcement-camera-locations>`__, but it's easier to get this information from the citation data than from a PDF. Each citation record includes a latitude and longitude, but it's only specified to three decimal places. This results in each citation's location being "snapped" to a finite set of points within DC. It looks like this:

.. container:: float wp-block-image aligncenter size-full

   |image6|

When an ATE camera is deployed in a particular location, every citation it issues gets the same latitude/longitude pair. This lets us examine not only the number of camera locations, but the number of days that a camera was in a particular location.

One last puzzle piece before we get started in earnest: DC's wards. The city is divided into eight of them. And while you'd be a fool to call anything having to do with race in DC "simple", the wards do make some kinds of equity analysis straightforward, both because they have approximately equal populations:

.. container:: float wp-block-image aligncenter size-full

   |image7|

And because wards 7 and 8--east of the Anacostia River--are the parts of the city with the highest percentage of Black people. They're also the city's `poorest wards <https://mchb.tvisdata.hrsa.gov/Narratives/Overview/258318d0-8dbe-46fd-9a77-385b6753e1c7>`__.

.. container:: float wp-block-image aligncenter size-full

   |image8|

With these facts in hand, we can start looking at the distribution and impact of the city's ATE cameras.

.. raw:: html

   <ul>

.. raw:: html

   </p>

.. raw:: html

   <li>

Are ATE cameras being placed equitably?

.. raw:: html

   </li>

.. raw:: html

   <li>

Are ATE cameras issuing citations equitably?

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. container:: float wp-block-image aligncenter size-full

   |image9|

.. container:: float wp-block-image aligncenter size-full

   |image10|

.. container:: float wp-block-image aligncenter size-full

   |image11|

A high *camera location:camera days* ratio suggests deployment of fewer fixed cameras and more mobile cameras. A high *citation:camera day* ratio suggests cameras are being deployed in locations that generate more citations, on average.

We can look at this last question in more detail, calculating a *citations per camera day* metric for each location and mapping it. Here's the result:

.. container:: float wp-block-image aligncenter size-full

   |image12|

Some of those overlapping circles should probably be combined (and made even larger!): they represent cameras with very slightly different locations that are examining traffic traveling in both directions; or stretches where mobile cameras have been moved up and down the road by small increments. Still, this is enough to be interesting.

Say, where were those DCPC study "outlier tracts" again?

.. container:: float wp-block-image aligncenter size-full

   |image13|

Area residents will probably have already mentally categorized the largest pink circles above: they're highways. Along the Potomac, they're the spots where traffic from 395 and 66 enter the city. Along the Anacostia, they trace 295. In ward 5, they trace New York Avenue's route out of the city and toward Route 50, I-95, and the BW Parkway. Other notable spots include an area near RFK Stadium where the roads are wide and empty; the often grade-separated corridor along North Capitol Street; and various locations along the 395 tunnel.

We can look at this analytically using OpenStreetMap data. Speed limit data would be nice, but it's famously spotty in OSM. The next best thing is *road class*, which is defined by OSM data's "highway" tag. This is the value that determines whether a line in the database gets drawn as a skinny gray alley or a thick red interstate. It's not perfect--it reflects human judgments about how something should be visually represented, not an objective measurement of some underlying quality--but it's not a bad place to start. You can find a complete explanation of the possible values for this tag `here <https://wiki.openstreetmap.org/wiki/Key:highway#Roads>`__. I used these six, which are listed from the largest kind of road to the smallest:

.. raw:: html

   <ol>

.. raw:: html

   </p>

.. raw:: html

   <li>

motorway

.. raw:: html

   </li>

.. raw:: html

   <li>

trunk

.. raw:: html

   </li>

.. raw:: html

   <li>

primary

.. raw:: html

   </li>

.. raw:: html

   <li>

secondary

.. raw:: html

   </li>

.. raw:: html

   <li>

tertiary

.. raw:: html

   </li>

.. raw:: html

   <li>

residential

.. raw:: html

   </li>

.. raw:: html

   </ol>

I stopped at "residential" for a reason. As described above, camera locations are snapped to a grid. That snapping means that when we ask PostGIS for the class of the nearest road for each camera location, we'll get back some erroneous data. If you go below the "residential" class you start including alleys, and the misattribution problem becomes overwhelming.

But "residential" captures what we're interested in. When we assign each camera location to a road class, we get the following:

.. container:: float wp-block-image aligncenter size-full

   |image14|

How does this compare to human-issued speed citation locations? I'm glad you asked:

.. container:: float wp-block-image aligncenter size-full

   |image15|

The delta between these tells the tale:

.. container:: float wp-block-image aligncenter size-full

   |image16|

ATE is disproportionately deployed on big, fast roads. And although OSM speed limit coverage isn't great, the data we do have further validates this, showing that ATE citation locations have an average ``maxspeed`` of 33.2 mph versus 27.9 for human citations.

Keep in mind that this is for citation *locations*. When we look at citations per location it becomes even more obvious that road class is overwhelmingly important.

.. container:: float wp-block-image aligncenter size-full

   |image17|

ATE is disproportionately deployed on big, fast roads. And ATE cameras deployed on big, fast roads generate disproportionately large numbers of citations.

But also: big, fast roads disproportionately carry non-local traffic. **This brings into question the entire idea of analyzing ATE equity impact by examining camera-adjacent populations.**

Stuff that didn't work
----------------------

None of this is how I began my analysis. My initial plan was considerably fancier. I created a sample of human speed enforcement locations and ATE enforcement locations and constructed some independent variables to accompany each: the nearby Black population percentage; the number of crashes (of varying severity) in that location in the preceding six months; the distance to one of DC's officially-designated `injury corridors <https://dcgis.maps.arcgis.com/apps/instant/media/index.html?appid=163f543d068340bc8c2b420030130c2b>`__. The idea was to build a logit classifier, then look at the coefficients associated with each IV to determine their relative importance in predicting whether a location was an example of human or ATE speed enforcement.

.. container:: float wp-block-image aligncenter size-full

   |image18|

But it didn't work! My confusion matrix was badly befuddled; my ROC curve AUC was a dismal 0.57 (0.5 means your classifier is as good as a coin flip). I couldn't find evidence that those variables are what determine ATE placement.

The truth is boring
-------------------

Traffic cameras get put on big, fast roads where they generate a ton of citations. Score one for the braindead ATE revenue truthers, I guess?

It is true that those big, fast roads are disproportionately in the city's Black neighborhoods. It's perfectly legitimate to point out the ways that highway placement and settlement patterns reflect past and present racial inequities--`DC is a historically significant exemplar of it, in fact <https://encyclopediavirginia.org/white-mans-road-thru-black-mans-home/>`__. But ATE placement is occurring in the context of that legacy, not causing it.

Besides, it's not even clear that the drivers on those highways are themselves disproportionately Black. That's a question worth asking, but neither I nor the DCPC study have the data necessary to answer it.

The Uncanny Efficacy of Equity Arguments
----------------------------------------

Before we leave this topic behind entirely, I want to briefly return to the idea of cognitive dissonance and its role in producing studies and narratives like the one I've just spent so many words and graphs trying to talk you out of.

The amazing thing about **actually, that thing is racist** content is that it attracts both people who dislike **that thing** and want to resolve dissonance by having their antipathy validated; AND people who like the **thing**. Arguably, it's more effective on that second group, because it introduces dissonance that they will be unable to resolve unless they engage with the argument. It's such a powerful effect that I knew it was happening to me the entire time I was writing this! And yet I kept typing!

I think it's rare for this strategy to be pursued cynically, or even deliberately. But it is an evolutionarily successful tactic for competing in an ever-more-intense attention economy. And the 2018 DCPC study debuted just as it was achieving takeoff in scholarly contexts:

.. container:: float wp-block-image aligncenter size-full

   |image19|

None of this is to say that racism isn't real or important. Of course it is! That's why the tactic works. But that fact is relatively disconnected from the efficacy of the rhetorical tactic, which can often be used to pump around attention (and small amounts of money) by applying and removing dissonance regardless of whether or not there's an underlying inequity--and without doing anything to resolve the inequity when it's truly present.

Speed cameras are good, stop worrying about it
----------------------------------------------

Speeding kills and maims people.

Speed cameras discourage speeding.

Getting tickets sucks, nobody's a perfect driver, but ATE cameras in DC don't cite you unless you're going 10 mph over the limit. It's truly not asking that much.

Please drive safely. And please don't waste your energy feeling guilty about insisting that our neighbors drive safely, too.

*map data, excluding DCPC, (c) OpenStreetMap (c) Mapbox*

.. |image1| image:: /static/2024/04/image-3-1024x337.png
   :class: wp-image-3513
   :target: /static/2024/04/image-3.png
.. |image2| image:: /static/2024/04/image-4.png
   :class: wp-image-3514
   :target: /static/2024/04/image-4.png
.. |image3| image:: /static/2024/04/image-5.png
   :class: wp-image-3515
   :target: /static/2024/04/image-5.png
.. |image4| image:: /static/2024/04/image-6.png
   :class: wp-image-3516
   :target: /static/2024/04/image-6.png
.. |image5| image:: /static/2024/04/image-7.png
   :class: wp-image-3517
   :target: /static/2024/04/image-7.png
.. |image6| image:: /static/2024/04/image-10.png
   :class: wp-image-3520
   :target: /static/2024/04/image-10.png
.. |image7| image:: /static/2024/04/image-11.png
   :class: wp-image-3521
   :target: /static/2024/04/image-11.png
.. |image8| image:: /static/2024/04/image-13.png
   :class: wp-image-3523
   :target: /static/2024/04/image-13.png
.. |image9| image:: /static/2024/04/image-14.png
   :class: wp-image-3524
   :target: /static/2024/04/image-14.png
.. |image10| image:: /static/2024/04/image-15.png
   :class: wp-image-3525
   :target: /static/2024/04/image-15.png
.. |image11| image:: /static/2024/04/image-16.png
   :class: wp-image-3526
   :target: /static/2024/04/image-16.png
.. |image12| image:: /static/2024/04/image-17.png
   :class: wp-image-3527
   :target: /static/2024/04/image-17.png
.. |image13| image:: /static/2024/04/image-18.png
   :class: wp-image-3528
   :target: /static/2024/04/image-18.png
.. |image14| image:: /static/2024/04/image-24.png
   :class: wp-image-3534
   :target: /static/2024/04/image-24.png
.. |image15| image:: /static/2024/04/image-26.png
   :class: wp-image-3536
   :target: /static/2024/04/image-26.png
.. |image16| image:: /static/2024/04/image-27.png
   :class: wp-image-3537
   :target: /static/2024/04/image-27.png
.. |image17| image:: /static/2024/04/image-28.png
   :class: wp-image-3538
   :target: /static/2024/04/image-28.png
.. |image18| image:: /static/2024/04/image-23.png
   :class: wp-image-3533
   :target: /static/2024/04/image-23.png
.. |image19| image:: /static/2024/04/image-1.png
   :class: wp-image-3511
   :target: /static/2024/04/image-1.png
