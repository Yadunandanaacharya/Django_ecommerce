# Generated by Django 3.1.1 on 2020-10-04 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_auto_20201004_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='cutomer',
            new_name='customer',
        ),
    ]