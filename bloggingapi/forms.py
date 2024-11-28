from django.forms import ModelForm
from django import forms
from .models import *
# from django_ckeditor_5.widgets import CKEditor5Widget
class BloggingForm(forms.ModelForm):

    class Meta:
        model=Blogging
        fields='__all__'

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=Category
        fields='__all__'
        
        


