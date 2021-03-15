from .models import Comment,Blog
from django import forms
from django_summernote.widgets import SummernoteWidget
	

class postForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'slug', 'post_pic','body')
		widgets = {
			'body':SummernoteWidget(),
		}


        