
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.widgets import Media
""" from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token """

####################################################################################
#############                     Modelos Iniciales                #################
####################################################################################

class Category(models.Model):
    id_category_product = models.AutoField(db_column='ID_CATEGORY_PRODUCT', primary_key=True)  # Field name made lowercase.
    category_vehicle = models.CharField(db_column='ID_CATEGORY_VEHICLE', max_length=20)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    #media = models.FileField(upload_to='carpeta/') 
    class Meta:
        managed = True
        db_table = 'category'
    
    def __str__(self):
        return f'{self.category_name}'

class Quotes(models.Model):
    id_quote = models.AutoField(db_column='ID_QUOTE', primary_key=True)  # Field name made lowercase.
    
    #Utilizado para almacenar los valores de los productos en forma de array
    description = models.CharField(db_column='DESCRIPTION', max_length=100, blank=True, null=True)

    date = models.DateTimeField(db_column='DATE', auto_now_add=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'quotes'
    

    def __str__(self):
        return f'{self.id_quote}'

class Role(models.Model):
    id_role = models.AutoField(db_column='ID_ROLE', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'role'
    

    def __str__(self):
        return f'{self.role_name}'


class Suppliers(models.Model):
    id_supplier = models.AutoField(db_column='ID_SUPPLIER', primary_key=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='SUPPLIER_NAME', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    conctact_name = models.CharField(db_column='CONCTACT_NAME', max_length=150)  # Field name made lowercase.
    landline = models.CharField(db_column='LANDLINE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=150)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'suppliers'
    

    def __str__(self):
        return f'{self.supplier_name}'


gender_options = [
    ('M', 'Masculino'),
    ('F', 'Femenino')
]

class Users(AbstractUser):
    id_user = models.AutoField(db_column='ID_USER', primary_key=True)  # Field name made lowercase.
    id_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='ID_ROLE')  # Field name made lowercase.
    id_card = models.CharField(db_column='ID_CARD', unique=True, max_length=10)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, null=False, blank=False, choices=gender_options)  # Field name made lowercase.
    born_date = models.DateTimeField(db_column='BORN_DATE')  # Field name made lowercase.
    landline = models.CharField(db_column='LANDLINE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOVILE_PHONE', max_length=15)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=100)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return f'{self.id_user}'



class Product(models.Model):
    id_product = models.AutoField(db_column='ID_PRODUCT', primary_key=True)  # Field name made lowercase.
    id_supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='ID_SUPPLIER')  # Field name made lowercase.
    id_category_product = models.ForeignKey(Category, models.DO_NOTHING, db_column='ID_CATEGORY_PRODUCT', related_name='FK_ID_CATEGORY_PRODUCT')  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=100)  # nombre del producto
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Descripción del producto
    price = models.DecimalField(db_column='PRICE', max_digits=12, decimal_places=2)  # Precio del producto
    brand = models.CharField(db_column='BRAND', max_length=100, blank=True, null=True)  # marca
    availability = models.IntegerField(db_column='AVAILABILITY', blank=True, null=True)  # Tiempo que demora en tenerse el producto a disposición
    registration_date = models.DateTimeField(db_column='REGISTRATION_DATE',auto_now_add=True)  # última fecha de modificación del producto
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED',auto_now=True) 
    #Añado estas tres para poder hacer distinct
    brand_vehicle = models.CharField(db_column='BRAND_VEHICLE', max_length=100, blank=True, null=True)
    model_vehicle = models.CharField(db_column='MODEL_VEHICLE', max_length=100, blank=True, null=True)
    year_vehicle = models.CharField(db_column='YEAR_VEHICLE', max_length=100, blank=True, null=True)
    part_number = models.CharField(db_column='PART_NUMBER', max_length=100, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'product'
        unique_together = (('id_product', 'id_supplier'),)

    def __str__(self):
        return f'{self.product_name}'

class qDetails(models.Model):
    id_qdetails = models.AutoField(db_column='ID_qdetails', primary_key=True)
    id_quote = models.ForeignKey(Quotes, models.DO_NOTHING, db_column='ID_QUOTE')  # Field name made lowercase.
    id_product = models.ForeignKey(Product, models.DO_NOTHING, db_column='ID_PRODUCT', related_name='FK_ID_PRODUCT')  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'qdetails'
        unique_together = (('id_quote', 'id_product'),)

    
    def __str__(self):
        return f'{self.id_qdetails}'

#Tabla para guardar archivos
class ProductFiles(models.Model):
    id_pfiles = models.AutoField(db_column='ID_PFILES', primary_key=True)  # Field name made lowercase.
    name_pfiles = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    productfile = models.FileField(upload_to='productsFiles/')

    class Meta:
        managed = True
        db_table = 'productfile'
    
    def __str__(self):
        return f'{self.id_pfiles}'


####################################################################################
#############                     Modelos para APIS                #################
############# Importante: En el caso de tener que hacer           ##################
############# modificaciones a la base de datos, comentar todo el ##################
############# código posterior                                    ##################
####################################################################################


class ProductSupplierJoin(models.Model):
    #Datos importantes del producto
    id_product = models.IntegerField(db_column='ID_PRODUCT')
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=100)  # nombre del producto
    price = models.DecimalField(db_column='PRICE', max_digits=12, decimal_places=2)  # Precio del producto
    brand = models.CharField(db_column='BRAND', max_length=100, blank=True, null=True)  # marca
    availability = models.IntegerField(db_column='AVAILABILITY', blank=True, null=True)  # Tiempo que demora en tenerse el producto a disposición en días
    brand_vehicle = models.CharField(db_column='BRAND_VEHICLE', max_length=100, blank=True, null=True)
    model_vehicle = models.CharField(db_column='MODEL_VEHICLE', max_length=100, blank=True, null=True)
    year_vehicle = models.CharField(db_column='YEAR_VEHICLE', max_length=100, blank=True, null=True)
    part_number = models.CharField(db_column='PART_NUMBER', max_length=100, blank=True, null=True)
    #Datos importantes del Proveedor
    id_supplier = models.IntegerField(db_column='ID_SUPPLIER')
    supplier_name = models.CharField(db_column='SUPPLIER_NAME', max_length=100)
    conctact_name = models.CharField(db_column='CONCTACT_NAME', max_length=150)
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=100, blank=True, null=True)  # Field name made lowercase.




