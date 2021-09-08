
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Category(models.Model):
    id_category_product = models.AutoField(db_column='ID_CATEGORY_PRODUCT', primary_key=True)  # Field name made lowercase.
    id_category_vehicle = models.CharField(db_column='ID_CATEGORY_VEHICLE', max_length=10)  # Field name made lowercase.
    catgory_name = models.CharField(db_column='CATGORY_NAME', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'category'
        unique_together = (('id_category_product', 'id_category_vehicle'),)

class Quotes(models.Model):
    id_quote = models.AutoField(db_column='ID_QUOTE', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=100)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=9, decimal_places=4)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'quotes'

class Role(models.Model):
    id_role = models.AutoField(db_column='ID_ROLE', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'role'


class Suppliers(models.Model):
    id_supplier = models.AutoField(db_column='ID_SUPPLIER', primary_key=True)  # Field name made lowercase.
    supplier_name = models.CharField(db_column='SUPPLIER_NAME', max_length=100)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    conctact_name = models.CharField(db_column='CONCTACT_NAME', max_length=100)  # Field name made lowercase.
    landline = models.CharField(db_column='LANDLINE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enmail = models.CharField(db_column='ENMAIL', max_length=100)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=100)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=100)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'suppliers'

#USUARIOS

class otrousuario(User):
    name_lastname = models.CharField(db_column='NAME_LASTNAME', max_length=150)
    country = models.CharField(db_column='COUNTRY', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return f'{self.name_lastname}'



class usuarioManager(BaseUserManager):
    def create_user(self, id_role, idcard, name_lastname, gender, born_date, landline, movile_phone, email, user, last_acces, city, province, country, password=None):
        if not email:
            raise ValueError('El usuario debe tener correo')
        
        usuario = self.model(
            id_role = id_role, 
            idcard = idcard,
            user = user,
            email = self.normalize_email(email),
            name_lastname = name_lastname,
            gender = gender,
            born_date = born_date,
            landline = landline,
            last_acces = last_acces,
            movile_phone = movile_phone
        )

        usuario.set_password(password)
        usuario.save()
        return usuario


class Users(AbstractBaseUser):
    id_user = models.AutoField(db_column='ID_USER', primary_key=True)  # Field name made lowercase.
    id_role = models.ForeignKey(Role, models.DO_NOTHING, db_column='ID_ROLE', blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(db_column='IDCARD', unique=True, max_length=10)  # Field name made lowercase.
    name_lastname = models.CharField(db_column='NAME_LASTNAME', max_length=150)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    born_date = models.DateTimeField(db_column='BORN_DATE')  # Field name made lowercase.
    landline = models.CharField(db_column='LANDLINE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    movile_phone = models.CharField(db_column='MOVILE_PHONE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100)  # Field name made lowercase.
    user = models.CharField(db_column='USER', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255)  # Field name made lowercase.
    last_acces = models.DateTimeField(db_column='LAST_ACCES')  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=100)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=100)  # Field name made lowercase.
    objects = usuarioManager()
    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return f'{self.name_lastname}'

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)








class Product(models.Model):
    id_product = models.AutoField(db_column='ID_PRODUCT', primary_key=True)  # Field name made lowercase.
    id_supplier = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='ID_SUPPLIER')  # Field name made lowercase.
    id_category_product = models.ForeignKey(Category, models.DO_NOTHING, db_column='ID_CATEGORY_PRODUCT', related_name='FK_ID_CATEGORY_PRODUCT', blank=True, null=True)  # Field name made lowercase.
    id_category_vehicle = models.ForeignKey(Category, models.DO_NOTHING, db_column='ID_CATEGORY_VEHICLE', related_name='FK_ID_CATEGORY_VEHICLE', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='BRAND', max_length=100, blank=True, null=True)  # Field name made lowercase.
    availability = models.IntegerField(db_column='AVAILABILITY', blank=True, null=True)  # Field name made lowercase.
    registration_date = models.DateTimeField(db_column='REGISTRATION_DATE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'product'
        unique_together = (('id_product', 'id_supplier'),)

class qDetails(models.Model):
    id_qdetails = models.AutoField(db_column='ID_qdetails', primary_key=True)
    id_quote = models.ForeignKey(Quotes, models.DO_NOTHING, db_column='ID_QUOTE')  # Field name made lowercase.
    id_product = models.ForeignKey(Product, models.DO_NOTHING, db_column='ID_PRODUCT', related_name='FK_ID_PRODUCT')  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=9, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'qdetails'
        unique_together = (('id_quote', 'id_product'),)

"""class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'"""