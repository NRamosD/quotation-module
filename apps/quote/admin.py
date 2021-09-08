from django.contrib import admin
from .models import Users, Role, otrousuario
# Register your models here.
admin.site.register(Users)
admin.site.register(Role)
admin.site.register(otrousuario)