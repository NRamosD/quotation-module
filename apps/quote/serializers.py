from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers
from .models import Users, Category, Quotes, Role, Suppliers, Product, qDetails
from rest_framework.authtoken.models import Token

from apps.quote import models


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)
    class Meta:
        model = get_user_model()
        #fields = [ 'id_user','email', 'username', 'password']
        #fields = ('__all__')
        exclude = ('groups','user_permissions','is_superuser','is_staff')
        #extra_kwargs = {'password': {'write_only': True, 'requiredd':True}} #extra_kwargs: para que no se vea en la solicitud
    
    def create(self, validated_data):
        usr = Users.objects.create_user(**validated_data)
        usr.set_password(validated_data['password'])
        usr.save()
        Token.objects.create(user=usr)
        return usr

class CategorySerializer(serializers.ModelSerializer):
    category_vehicle = serializers.CharField(required=True, max_length=20)
    category_name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True, max_length=200)

    class Meta:
        model = Category
        fields = ('__all__')

class QuotesSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()
    total = serializers.DecimalField(max_digits=12, decimal_places=3)
    class Meta:
        model = Quotes
        fields = ('__all__')

class RoleSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(max_length=200)
    class Meta:
        model = Role
        fields = ('__all__')

class SupplierSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(max_length=200)
    conctact_name = serializers.CharField(required=True, max_length=150)
    landline = serializers.CharField(max_length=15)
    mobile_phone = serializers.CharField(max_length=15)
    email =serializers.CharField(required=True, max_length=150)
    address = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=100)
    province = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    
    class Meta:
        model = Suppliers
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True,max_length=100)
    description = serializers.CharField(max_length=200)
    price = serializers.DecimalField(required=True, max_digits=12, decimal_places=3)
    brand = serializers.CharField(max_length=100)
    availability = serializers.IntegerField()
    registration_date = serializers.DateTimeField()
    last_modified = serializers.DateTimeField()
    class Meta:
        model = Product
        fields = ('__all__')

class qDetailsSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    subtotal = serializers.DecimalField(required = True, max_digits=12, decimal_places=3)
    class Meta:
        model = qDetails
        fields = ('__all__')
