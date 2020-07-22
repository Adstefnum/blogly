from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('',views.IndexView.as_view(),name = "index"),
	path('(?P<pk>[0-9]+)/',views.post_detail,name = "post"),
	]