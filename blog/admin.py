from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','body','email','post','created_on','active')
	list_filter = ('active','created_on')
	search_fields = ('name','email','body')
	actions = ['approve','remove']

	def approve(self,request,query_set):
		query_set.update(active = True)

	def remove(self,request,query_set):
		query_set.update(active = False)
