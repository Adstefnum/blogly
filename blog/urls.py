from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('',views.IndexView.as_view(),name = "index"),
	path(r'^(?P<pk>[0-9]+)/$',views.PostView.as_view(),name = "post"),
    ]