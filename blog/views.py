from django.views.generic.edit import View
from django.views.generic import ListView, DetailView
from .forms import commentForm
from django.shortcuts import render,get_object_or_404
from .models import *

class IndexView(ListView):
	template_name = "blog/index.html"

	def get_queryset(self):
		return Blog.objects.all()[3:7:-1]

def post_detail(request, pk):
    template_name = 'blog/post.html'
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comment_set.filter(active=True)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = commentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.post_id = pk
            new_comment.save()
    else:
        comment_form = commentForm()
 
    return render(request, template_name, {'blog': blog,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form}) 

	

