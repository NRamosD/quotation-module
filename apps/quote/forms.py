from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets
from .models import Product, ProductFiles, Users
from apps.quote.models import Product
from django.db.models.base import Model

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




class CreateUserForm(forms.ModelForm):
    class Meta:
        model= Users
        fields = ['email','username','password','first_name','last_name','id_card','gender','born_date','landline','mobile_phone','city','province','country','id_role']
        labels={
            'email': 'Correo Electronico',
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'id_card': 'Cédula de identidad(sin guión)',
            'gender':'Género',
            'born_date': 'Fecha de Nacimiento',
            'landline':'Teléfono fijo',
            'mobile_phone': 'Celular',
            'city': 'Ciudad de Origen',
            'province': 'Provincia de origen',
            'country': 'País de origen'
        }
        widgets= {
            'email': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electrónico',
                    'id': 'email'
                }
            ),
              'username': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre de usuario',
                    'id': 'username'
                }
            ),
              'password': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contraseña',
                    'id': 'password',
                    'type': 'password'
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
              'id_card': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'cédula sin guión',
                    'id': 'id_card'
                }
            ),
              'gender': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Género',
                    'id': 'gender'
                }
            ),
                'born_date': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Fecha de Nacimiento',
                    'id': 'born_date',
                    'type':'date'
                }
            ),
                'landline': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Teléfono fijo',
                    'id': 'landline'
                }
            ),
              'mobile_phone': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Teléfono',
                    'id': 'mobile_phone'
                }
            ),
              'city': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ciudad de procedencia',
                    'id': 'city'
                }
            ),
              'province': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Provincia de Procedencia',
                    'id': 'province'
                }
            ),
              'country': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'País',
                    'id': 'country'
                }
            )
        }
