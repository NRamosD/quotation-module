# Generated by Django 3.2.6 on 2021-08-07 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category_product', models.AutoField(db_column='ID_CATEGORY_PRODUCT', primary_key=True, serialize=False)),
                ('id_category_vehicle', models.CharField(db_column='ID_CATEGORY_VEHICLE', max_length=10)),
                ('catgory_name', models.CharField(db_column='CATGORY_NAME', max_length=100)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=200)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
                'unique_together': {('id_category_product', 'id_category_vehicle')},
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id_quote', models.AutoField(db_column='ID_QUOTE', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=100)),
                ('date', models.DateTimeField(db_column='DATE')),
                ('total', models.DecimalField(db_column='TOTAL', decimal_places=4, max_digits=9)),
            ],
            options={
                'db_table': 'quotes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.AutoField(db_column='ID_ROLE', primary_key=True, serialize=False)),
                ('role_name', models.CharField(db_column='ROLE_NAME', max_length=50)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=200)),
            ],
            options={
                'db_table': 'role',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id_supplier', models.AutoField(db_column='ID_SUPPLIER', primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(db_column='SUPPLIER_NAME', max_length=100)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=200, null=True)),
                ('conctact_name', models.CharField(db_column='CONCTACT_NAME', max_length=100)),
                ('landline', models.CharField(blank=True, db_column='LANDLINE', max_length=10, null=True)),
                ('mobile_phone', models.CharField(blank=True, db_column='MOBILE_PHONE', max_length=10, null=True)),
                ('enmail', models.CharField(db_column='ENMAIL', max_length=100)),
                ('address', models.CharField(blank=True, db_column='ADDRESS', max_length=100, null=True)),
                ('city', models.CharField(db_column='CITY', max_length=100)),
                ('province', models.CharField(db_column='PROVINCE', max_length=100)),
                ('country', models.CharField(db_column='COUNTRY', max_length=100)),
            ],
            options={
                'db_table': 'suppliers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(db_column='ID_USER', primary_key=True, serialize=False)),
                ('idcard', models.CharField(db_column='IDCARD', max_length=10, unique=True)),
                ('name_lastname', models.CharField(db_column='NAME_LASTNAME', max_length=150)),
                ('gender', models.CharField(blank=True, db_column='GENDER', max_length=1, null=True)),
                ('born_date', models.DateTimeField(db_column='BORN_DATE')),
                ('landline', models.CharField(blank=True, db_column='LANDLINE', max_length=10, null=True)),
                ('movile_phone', models.CharField(blank=True, db_column='MOVILE_PHONE', max_length=10, null=True)),
                ('email', models.CharField(db_column='EMAIL', max_length=100)),
                ('user', models.CharField(db_column='USER', max_length=50)),
                ('password', models.CharField(db_column='PASSWORD', max_length=50)),
                ('last_acces', models.DateTimeField(db_column='LAST_ACCES')),
                ('city', models.CharField(db_column='CITY', max_length=100)),
                ('province', models.CharField(db_column='PROVINCE', max_length=100)),
                ('country', models.CharField(db_column='COUNTRY', max_length=100)),
                ('id_role', models.ForeignKey(blank=True, db_column='ID_ROLE', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='quote.role')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(db_column='ID_PRODUCT', primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, db_column='PRODUCT_NAME', max_length=100, null=True)),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, db_column='PRICE', decimal_places=4, max_digits=9, null=True)),
                ('brand', models.CharField(blank=True, db_column='BRAND', max_length=100, null=True)),
                ('availability', models.IntegerField(blank=True, db_column='AVAILABILITY', null=True)),
                ('registration_date', models.DateTimeField(db_column='REGISTRATION_DATE')),
                ('id_category_product', models.ForeignKey(blank=True, db_column='ID_CATEGORY_PRODUCT', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_ID_CATEGORY_PRODUCT', to='quote.category')),
                ('id_category_vehicle', models.ForeignKey(blank=True, db_column='ID_CATEGORY_VEHICLE', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_ID_CATEGORY_VEHICLE', to='quote.category')),
                ('id_supplier', models.ForeignKey(db_column='ID_SUPPLIER', on_delete=django.db.models.deletion.DO_NOTHING, to='quote.suppliers')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
                'unique_together': {('id_product', 'id_supplier')},
            },
        ),
        migrations.CreateModel(
            name='qDetails',
            fields=[
                ('id_qdetails', models.AutoField(db_column='ID_qdetails', primary_key=True, serialize=False)),
                ('amount', models.IntegerField(db_column='AMOUNT')),
                ('subtotal', models.DecimalField(db_column='SUBTOTAL', decimal_places=4, max_digits=9)),
                ('id_product', models.ForeignKey(db_column='ID_PRODUCT', on_delete=django.db.models.deletion.DO_NOTHING, related_name='FK_ID_PRODUCT', to='quote.product')),
                ('id_quote', models.ForeignKey(db_column='ID_QUOTE', on_delete=django.db.models.deletion.DO_NOTHING, to='quote.quotes')),
            ],
            options={
                'db_table': 'qdetails',
                'managed': True,
                'unique_together': {('id_quote', 'id_product')},
            },
        ),
    ]
