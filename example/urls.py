from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    ('', include('profiles.urls')),
    ('^friends/', include('friends.urls')),
)


if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
