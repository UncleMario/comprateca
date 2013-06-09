from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',

    url(r'^logout/$', logout, {'next_page' : '/'}),

    url(r'^facebook/', include('django_facebook.urls')),

    url(r'^mvp/', include('comprateca.mvp.urls')),

    url(r'^$', 'direct_to_template', {'template':'mvp/home.html'}),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
