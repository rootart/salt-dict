from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from dictionary.views import IndexView
from dictionary.api import v1_api

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='homepage'),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
)

urlpatterns += patterns("django.views",
    url(r"%s(?P<path>.*)$" % settings.STATIC_URL[1:], "static.serve", {
        "document_root": settings.STATIC_ROOT,
        'show_indexes': True,
    }),
    url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "static.serve", {
        "document_root": settings.MEDIA_ROOT,
        'show_indexes': True,
    }),
)
