from django.views.generic.edit import View
from django.views.generic import ListView, DetailView
from .forms import *
from django.shortcuts import render,get_object_or_404, redirect
from django.http import  HttpResponseRedirect
from .models import *


class IndexView(ListView):
	template_name = "blog/index.html"

	def get_queryset(self):
		return Blog.objects.all()

def post_detail(request, pk):
    template_name = 'blog/article.html'
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

def write_detail(request):
    template_name = 'blog/write.html'
    
    if request.method == 'POST':

        post_form = postForm(request.POST)
        
        if post_form.is_valid():
            post_form.save()
            #redirect to the posted blog
            return redirect('blog:index') 

    else:
        post_form = postForm()
 
    return render(request, template_name, {'post_form': post_form}) 


def author_detail(request):
    template_name = 'blog/author.html'
    
    if request.method == 'POST':
        pass 

