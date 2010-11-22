from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from pustkow_osiedle.page.views import *
import settings 

urlpatterns = patterns('', 
                       (r'^fotografie/?$', fotografie),

                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/(.*)', admin.site.root),
                       )

urlpatterns += patterns('django.views.generic',
                        (r'^$', 'simple.redirect_to', {'url': '/obecnie/'}),
                        )


if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                            )
