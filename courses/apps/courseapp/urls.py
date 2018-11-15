from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^process', views.process),
	url(r'^course/(?P<number>\d+$)', views.delete),
	url(r'^remove/(?P<number>\d+$)', views.remove)
	
	]
