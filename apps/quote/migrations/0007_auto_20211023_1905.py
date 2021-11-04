# Generated by Django 3.2.6 on 2021-10-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0006_auto_20211023_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qdetails',
            name='subtotal',
            field=models.DecimalField(db_column='SUBTOTAL', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='total',
            field=models.DecimalField(db_column='TOTAL', decimal_places=2, max_digits=12),
        ),
    ]
