from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Blog(models.Model):
   title = models.CharField(max_length=100, unique=True)
   slug = models.SlugField(max_length=100, unique=True)
   post_pic = models.ImageField(upload_to ='media/post_pics/', default =None )
   body = models.TextField()
   posted = models.DateTimeField(db_index=True, auto_now_add=True)

   def __str__(self):
   	return self.title

   def get_absolute_url(self):
      return reverse('blog:post', kwargs={'pk':self.pk})

class Comment(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   body = models.TextField(max_length=500)
   created_on = models.DateTimeField(db_index=True, default=now)
   post = models.ForeignKey(Blog,on_delete=models.CASCADE)
   active = models.BooleanField(default=True)
   parent = models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)

   class Meta:
      ordering = ['-created_on']

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('blog:post', kwargs={'pk':self.pk})



