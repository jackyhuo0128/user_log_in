from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'user_log_in.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^logincount/$', 'logincount.views.index'),
    #url(r'^logincount/(?P<user_id>\d+)/$', 'logincount.views.detail'),
    #url(r'^logincount/(?P<user_id>\d+)/results/$', 'logincount.views.results'),
    #url(r'^logincount/(?P<user_id>\d+)/vote/$', 'logincount.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('logincount.urls', namespace = 'logincount')),

)
