from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from .models import ProductFiles, Users

class ProductFilesForm(forms.ModelForm):
    class Meta:
        model = ProductFiles
        fields = ['name_pfiles', 'productfile' ]
    
class UserForm(forms.ModelForm):
    class Meta:
        model= Users
        fields = ['email','username','password','first_name','last_name','mobile_phone','city','province','country']
        labels={
            'email': 'Correo Electronico',
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
            'first_name': 'Nombre del User jeje',
            'last_name': 'Apellido',
            'mobile_phone': 'Celular',
            'city': 'Ciudad de Origen',
            'province': 'Provincia de origen',
            'country': 'Pais de origen'
        }
        widgets= {
            'email': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'correo',
                    'id': 'email'
                }
            ),
              'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'usuario',
                    'id': 'username'
                }
            ),
              'password': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contrasena',
                    'id': 'password'
                }
            ),
              'first_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Nombre del User',
                    'id': 'first_name'
                }
            ),
              'last_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Apellido',
                    'id': 'last_name'
                }
            ),
              'mobile_phone': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Telfono',
                    'id': 'mobile_phone'
                }
            ),
              'city': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'ciudad',
                    'id': 'city'
                }
            ),
              'province': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'pronvicia',
                    'id': 'province'
                }
            ),
              'country': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'paiss',
                    'id': 'country'
                }
            )
        }

