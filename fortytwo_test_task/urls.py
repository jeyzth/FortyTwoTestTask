from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    url(r'^$', include('hello.urls')),
    url(r'^css/$', include('hello.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^/', include('hello.urls')),
    url(r'^hello/', include('hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
