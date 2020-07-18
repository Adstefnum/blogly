from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comment,Blog

class IndexView(ListView):
	template_name = "blog/index.html"

	def get_queryset(self):
		return Blog.objects.all()[3:7:-1]

class PostView(DetailView):
	model = Blog
	template_name = "blog/post.html"
