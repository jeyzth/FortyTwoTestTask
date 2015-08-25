from django.conf.urls import patterns, url

from hello import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^editor$', views.editor, name='editor'),
    url(r'^requests10$', views.requests10, name='requests10'),
    url(r'^chknewreq$', views.chknewreq),
)
