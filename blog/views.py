from django.views.generic.edit import View
from django.views.generic import ListView, DetailView
from .forms import commentForm
from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponseRedirect
from .models import *

class IndexView(ListView):
	template_name = "blog/index.html"

	def get_queryset(self):
		return Blog.objects.all()[3:7:-1]

def post_detail(request, pk):
    template_name = 'blog/post.html'
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comment_set.filter(active=True,parent = None)
    new_comment =None
    
    if request.method == 'POST':
        comment_form = commentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.get(id=parent_id)
                if parent_qs:
                    parent_obj = parent_qs
                    
            new_comment = comment_form.save(commit=False)
            new_comment.parent = parent_obj
            new_comment.blog = blog
            new_comment.post_id = pk
            new_comment.save()

            return HttpResponseRedirect(blog.get_absolute_url()) 

    else:
        comment_form = commentForm()
 
    return render(request, template_name, {'blog': blog,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form}) 

	

