from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/$', views.post_edit, name='post_new'),
	url(r'^post/new/$', views.post_edit, name='post_new'),
]