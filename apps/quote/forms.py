from django import forms
from django.forms import ModelForm
from django.forms import fields, widgets
from .models import Category, Product, ProductFiles, Suppliers, Users
from django.db.models.base import Model

class ProductFilesForm(forms.ModelForm):
    class Meta:
        model = ProductFiles
        fields = ['name_pfiles', 'productfile' ]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['id_category_product' ,"category_name","category_vehicle","description"]
        labels = {
            "category_name": "Nombre de la Categoría",
            "category_vehicle": "Categoría de vehículo",
            "description": "Descripción"
        }
        widgets = {
            'category_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejm: Llantas, Frenos, etc.',
                    'id': 'category_name'
                }
            ),
            'category_vehicle': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejm: Liviano, Pesado, Dos Ruedas, etc.',
                    'id': 'category_vehicle'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Datos importantes de la categoría...',
                    'id': 'description'
                }
            )
        }



class SupplierForm(ModelForm):
    class Meta:
        model = Suppliers
        fields = ['id_supplier', "supplier_name","description","conctact_name",
                "landline","mobile_phone","email","address","city","province","country"
                ]
        labels = {
            "supplier_name": "Nombre de Empresa",
            "description": "Descripción",
            "conctact_name": "Encargado",
            "landline": "Teléfono Fijo",
            "mobile_phone": "Celular",
            "email": "Correo Electrónico",
            "address": "Dirección",
            "city": "Ciudad",
            "province": "Provincia",
            "country": "País"
        }
        widgets = {
            'supplier_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejm: Mansuera Quito',
                    'id': 'supplier_name'
                }
            ),
              'description': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Breves características del proveedor',
                    'id': 'description'
                }
            ),
              'conctact_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'José Delgado',
                    'id': 'contact_name'
                }
            ),
              'landline': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'062760399',
                    'id': 'landline'
                }
            ),
              'mobile_phone': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'5930999999999',
                    'id': 'mobile_phone'
                }
            ),
              'email': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'ejemplo@gmail.com',
                    'id': 'email'
                }
            ),
              'address': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejm: Av. Occidental N70-297 y, Quito 170134',
                    'id': 'address'
                }
            ),
                
                'city': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Quito',
                    'id': 'city'
                }
            ),
                
                'province': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número o código del producto',
                    'id': 'part_number'
                }
            ),
                
                'country': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número o código del producto',
                    'id': 'part_number'
                }
            )
            
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        #'registration_date','last_modified',
        fields = ['id_supplier', 'id_category_product', 'product_name', 'description',
                'price', 'brand','availability',
                'brand_vehicle','model_vehicle','year_vehicle','part_number'
                ]
        labels = {
            'id_supplier':'Proveedor',
            'id_category_product':'Categoría',
            'product_name':'Nombre del Producto', 
            'description':'Descripción',
            'price':'Precio', 
            'brand':'Marca',
            'availability':'Disponibilidad',
            'brand_vehicle':'Marca del Vehículo',
            'model_vehicle':'Modelo del Vehículo',
            'year_vehicle':'Año del Vehículo',
            'part_number':'Número de Parte'
        }
        widgets = {
            'product_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre del Producto',
                    'id': 'product_name'
                }
            ),
              'description': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Breves características del producto',
                    'id': 'description'
                }
            ),
              'price': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejem: 5.99',
                    'id': 'price',
                    'type': 'number'
                }
            ),
              'brand': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Marca del Producto',
                    'id': 'brand'
                }
            ),
              'availability': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Días de espera para recibir el producto',
                    'id': 'availability'
                }
            ),
              'brand_vehicle': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejm: Kía, Mazda, etc.',
                    'id': 'brand_vehicle'
                }
            ),
              'model_vehicle': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ejm: Sedan, Aveo, etc.',
                    'id': 'model_vehicle'
                }
            ),
                
                'part_number': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número o código del producto',
                    'id': 'part_number'
                }
            )
            
        }



class UserForm(ModelForm):
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
