from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Users
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)
    class Meta:
        model = get_user_model()
        fields = [ 'email', 'username', 'password']
        #fields = ('__all__')
        #exclude = ('groups','user_permissions')
        #extra_kwargs = {'password': {'write_only': True, 'required':True}} #extra_kwargs: para que no se vea en la solicitud
    
    def create(self, validated_data):
        usr = Users.objects.create_user(**validated_data)
        usr.set_password(validated_data['password'])
        usr.save()
        Token.objects.create(user=usr)
        return usr