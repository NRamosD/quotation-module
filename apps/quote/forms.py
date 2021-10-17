from django import forms
from django.forms import fields
from .models import ProductFiles

class ProductFilesForm(forms.ModelForm):
    class Meta:
        model = ProductFiles
        fields = ['name_pfiles', 'productfile' ]
    
    
