from django.conf.urls.defaults import *


urlpatterns = patterns('profiles.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^login/(?P<username>\w+)/$', 'login_as_user', name='login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='logout'),
    url(r'^profile/$', 'profile_detail', name='profile_detail'),
)