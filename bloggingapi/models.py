from django.db import models
# from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_title=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

class Blogging(models.Model):
    title=models.CharField(max_length=200)
    # content=models.TextField()
    # content=RichTextField()
    content=CKEditor5Field('Text',null=True,blank=True,config_name='extends')
    image=models.FileField(upload_to='static/uploads')
    created_at=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.CharField(max_length=250)
    post=models.ForeignKey(Blogging,on_delete=models.CASCADE,null=True)
    message=models.TextField()

    def __str__(self):
       return self.fullname

    