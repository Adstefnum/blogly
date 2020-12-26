from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('',views.IndexView.as_view(),name = "index"),
	path('(?P<pk>[0-9]+)/',views.post_detail,name = "post"),
	path('write/',views.write_detail,name = "write"),
	path('author/',views.author_detail,name = "author"),
	path('register/',views.register,name = "register"),
	#path('login/',views.login,name = "login"),
	]