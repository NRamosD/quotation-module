from django.contrib import admin
from .models import Category, Product, Quotes, Suppliers, Users, Role, qDetails, ProductFiles
# Register your models here.
admin.site.register(Users)
admin.site.register(Role)
admin.site.register(Product)
admin.site.register(Suppliers)
admin.site.register(Category)
admin.site.register(qDetails)
admin.site.register(Quotes)
admin.site.register(ProductFiles)