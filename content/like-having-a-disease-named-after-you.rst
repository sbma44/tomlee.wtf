like having a disease named after you
#####################################
:date: 2007-09-17 14:28
:author: admin
:category: tech
:slug: like-having-a-disease-named-after-you
:status: published
:save_as: 2007/09/17/like-having-a-disease-named-after-you/index.html
:url: 2007/09/17/like-having-a-disease-named-after-you/

`Drupal <http://www.drupal.org>`__ is excellent software, PHP-based though it may be. So there's a little thrill of excitement that occurs when you find what appears to be a genuine bug in a high-profile part of it. But that thrill is tempered when you realize that a) your clients don't care about the exotic nature of the problem, as they have already launched their website against your recommendation and b) all of the people who could help you appear to currently be on `planes to Barcelona <http://barcelona2007.drupalcon.org/>`__.

So I reproduce my plaintive IRC begging here not because I think it's likely to help (I know some Drupal hax0rs extraordinaire, but I don't think they're subscribed). No, this is just me crying out to the universe.

   | I've got a really weird issue with Views and profile fields. Essentially, a profile-heavy view intermittently stops returning any records. Resaving the view typically resolves the problem -- for a while. I haven't been able to determine the event that causes the view to break again, but it always does. Looking at the results from views_build_view('queries',..), it's clear that sometimes the module is forgetting to repeatedly join the query against profile_values.
   | for example, here's how the query looks when it's working: http://papernapkin.org/pastebin/view/2725
   | and here's how it looks when it's broken: http://papernapkin.org/pastebin/view/2726
   | in hook_views_query_alter this manifests itself as abbreviated 'tables' and 'tablequeue' properties in the query object. but adding code to that hook to manually alter those properties to the known-to-be-good version doesn't resolve the problem. so I'm at a loss. any ideas would be greatly appreciated.

It looks like I'll be dumping views and rewriting this page manually. Which, in turn, means that you can expect bitching about a SQL injection problem in this space in two or three days...
