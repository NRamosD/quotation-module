from rest_framework import serializers
from .models import Users
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        #fields = ['id', 'username', 'password', 'name_lastname','country']
        fields = ('__all__')
        #extra_kwargs = {'password': {'write_only': True, 'required':True}} #extra_kwargs: para que no se vea en la solicitud
    
    def create(self, validated_data):
        usr = Users.objects.create_user(**validated_data)
        #user.set_password(validated_data['password'])
        #user.save()
        #Token.objects.create(user=usr)
        return usr