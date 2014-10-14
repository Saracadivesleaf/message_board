from django.conf.urls import patterns, include, url
from django.contrib import admin
from liuyanban.views import message
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sacara.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^message/',message),
    url(r'^$','messageboard.views.msg_list_page'),
    
)
