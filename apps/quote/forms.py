from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import ProductFiles, Users

class ProductFilesForm(forms.ModelForm):
    class Meta:
        model = ProductFiles
        fields = ['name_pfiles', 'productfile' ]
    
class UserForm(forms.ModelForm):
    class Meta:
        Model= Users
        fields = "__all__"    
