from django import forms
from django.forms import fields
from .models import Category

class uploadFile(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'media' ]
    
    
