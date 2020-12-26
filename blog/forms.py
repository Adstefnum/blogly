from .models import Comment,Blog
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class regForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']
		
class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')
		widgets = {
			'body':SummernoteWidget(),
		}
	

class postForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'slug', 'post_pic','body')
		widgets = {
			'body':SummernoteWidget(),
		}


        