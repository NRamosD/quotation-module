from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "id_user",
            "id_role",
            "idcard",
            "name_lastname",
            "gender",
            "born_date",
            "landline",
            "movile_phone",
            "email",
            "user", 
            "password",
            "last_acces",
            "city",
            "province",
            "country"]
        extrakwargs = {'password': {'write_only': True, 'requiered':True}} #para que no se vea en la solicitud
    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user


