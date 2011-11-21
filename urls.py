from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from .page.views import *

urlpatterns = patterns('',
    (r'^fotografie/?$', fotografie),
    (r'^admin/(.*)', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic',
    (r'^$', 'simple.redirect_to', {'url': '/obecnie/'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
