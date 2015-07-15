from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/v1.0/resource/(?P<resource_id>\w+)[/]?$', views.RESTView.as_view(), name='my_rest_view'),
    url(r'^api/v1.0/resource[/]?$', views.RESTView.as_view(), name='my_rest_view'),
]
