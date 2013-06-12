from django.conf.urls import patterns, include, url

urlpatterns = patterns('comprateca.mvp.views',

    url(r'^article/$','article', name='post article'),

    url(r'^articles/$','all_articles', name='all articles'),

    url(r'^article/(?P<articleID>\d+)/$','view_article', name='view article'),

    url(r'^my-publications/$', 'my_publications', name='my publications'),

    url(r'^search/$', 'search', name='search'),

    url(r'^test/$','test_open_facebook', name="test"),
   
) 