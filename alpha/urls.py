from django.conf.urls import patterns, url
from alpha import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
				url(r'^bio/', views.bio, name='bio'))