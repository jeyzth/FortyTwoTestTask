from django.conf.urls import patterns, url

from hello import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^requests10$', views.requests10, name='requests10'),
)
