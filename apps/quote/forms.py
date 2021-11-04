from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets
from .models import Product, ProductFiles
from apps.quote.models import Product

class ProductFilesForm(forms.ModelForm):
    class Meta:
        model = ProductFiles
        fields = ['name_pfiles', 'productfile' ]
    
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'id_product',
            'id_supplier',
            'id_category_product',
            'product_name',
            'description',
            'price',
            'brand',
            'availability',
            #'registration_date',
            #'last_modified',
        ]
        labels = {
            'id_product':'ID producto',
            'id_supplier': 'ID proveedor',
            'id_category_product': 'ID categoria',
            'product_name': 'Nombre del Producto',
            'description':'Descripción',
            'price' : 'Precio',
            'brand': 'Marca',
            'availability': 'Disponibilidad',
            #'registration_date': 'Fecha de Registro',
            #'last_modified': 'Fecha de modificación',
        }
        widgets = {
            'id_product': forms.TextInput(attrs={'class':'form-control'}),
            'id_supplier': forms.Select(attrs={'class':'form-control'}),
            'id_category_product': forms.Select(attrs={'class':'form-control'}),
            'product_name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'availability': forms.TextInput(attrs={'class':'form-control'}),
            #'registration_date': forms.TextInput(attrs={'class':'form-control'}),
            #'last_modified': forms.TextInput(attrs={'class':'form-control'}),
        }

