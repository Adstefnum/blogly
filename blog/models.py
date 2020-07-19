from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
   title = models.CharField(max_length=100, unique=True)
   slug = models.SlugField(max_length=100, unique=True)
   post_pic = models.ImageField(upload_to ='media/post_pics/', default =None )
   body = models.TextField()
   posted = models.DateTimeField(db_index=True, auto_now_add=True)

   def __str__(self):
   	return self.title

class Comment(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   comment = models.TextField(max_length=500)
   posted = models.DateTimeField(db_index=True,  default=now)
   comments_post = models.ForeignKey(Blog,on_delete=models.CASCADE,default=1)

   def __str__(self):
      return self.name

class commentReply(models.Model):
   name = models.CharField(max_length=100)
   email = models.CharField(max_length=100)
   comment = models.TextField(max_length=500)
   posted = models.DateTimeField(db_index=True, default=now)
   comments_post = models.ForeignKey(Comment,on_delete=models.CASCADE,default=1)

   def __str__(self):
      return self.name