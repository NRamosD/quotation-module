from django.db import models


# Create your models here.

class ROLE(models.Model):
    id_role = models.Charfield(max_length=10, primary_key = True)
    role_name = models.Charfield(max_length=50, blank = False)
    description = models.Charfield(max_length=200, blank = False)
    def __str__(self):
        return f"id:{self.id_role} role_name:{self.role_name}"


class USERS(models.Model):
    #own
    id_user = models.CharField(max_length=10, primary_key = True)
    idcard = models.CharField(max_length=10, blank = False)
    name_lastname = models.CharField(max_length=150, blank = False)
    gender = models.CharField(max_length=1)
    born_date = models.DateTimeField(blank = False)
    landline = models.CharField(max_length=10)
    movile_phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100, blank = False)
    user = models.CharField(max_length=50, blank = False)
    password = models.CharField(max_length=50, blank = False)
    last_access = models.DateTimeField(blank = False)
    city = models.CharField(max_length=100, blank = False)
    province = models.CharField(max_length=100, blank = False)
    country = models.CharField(max_length=100, blank = False)
    #foreign
    id_role = models.ForeignKey(ROLE, on_delete = models.CASCADE, blank = False, related_name="id_role")
    

class CATEGORY(models.Model):
    id_category_product = models.CharField(max_length=10, primary_key = True)
    id_category_vehicle = models.CharField(max_length=10, blank = False)
    category_name = models.CharField(max_length=100, blank = False)
    description = models.CharField(max_length=200, blank = False)

class SUPPLIERS(models.Model):
    id_supplier = models.CharField(max_length=10, prymary_key = True)
    supplier_name = models.CharField(max_length=100, blank = False)
    description = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=100, blank = False)
    landline = models.CharField(max_length=10)
    mobile_phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100, blank = False)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank = False)
    province = models.CharField(max_length=100, blank = False)
    country = models.CharField(max_length=100, blank = False)

class PRODUCT(models.Model):
    class Meta:
        unique_together = ((id_product, id_supplier))

    #owns
    id_product = models.CharField(max_length=10)
    product_name = models.CharField(max_length=100, blank = False)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits = 9, decimal_places = 4, blank = False)
    brand = models.CharField(max_length=100)
    availability = models.IntegerField()
    registration_date = models.DateTimeField(blank = False)
    #foreigns
    id_supplier = models.ManyToManyField(SUPPLIERS, on_delete=models.CASCADE, blank=True, related_name="id_supplier")
    id_category_product = models.ForeignKey(CATEGORY, on_delete=models.CASCADE, related_name="id_category_product")
    id_category_vehicle = models.ForeignKey(CATEGORY, on_delete=models.CASCADE, related_name="id_category_vehicle")

class QUOTES(models.Model):
    id_quote = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, blank = False)
    date = models.models.DateTimeField(blank = False)
    total = models.DecimalField(max_digits = 9, decimal_places = 4, blank = False)

class QUOTES_DETAILS(models.Model):
    class Meta:
        unique_together = ((id_quote, id_product, id_supplier))
    
    id_quote = models.ManyToManyField(SUPPLIERS, on_delete=models.CASCADE, blank = True, related_name="id_quote")
    id_product = models.ManyToManyField(SUPPLIERS, on_delete=models.CASCADE, blank = True, related_name="id_product")
    id_supplier = models.ManyToManyField(SUPPLIERS, on_delete=models.CASCADE, blank = True, related_name="id_supplier")
    amount = models.IntegerField(blank = False)
    subtotal = models.DecimalField(max_digits = 9, decimal_places = 4, blank = False)




    

