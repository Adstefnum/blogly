from .models import Comment
from django import forms

class subscribeForm(forms.Form):
	email = forms.CharField(label='email', max_length=100)

class commentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')
	
	'''name = forms.CharField(widget=forms.TextInput ,label='Name', max_length=100, required = True)
	email = forms.EmailField(label='Email', required=True)#change thiswhen user authentication is enabled
	body = forms.CharField(label='Comment', max_length=100, widget=forms.Textarea, required = True)'''