# Generated by Django 3.1.1 on 2020-10-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomshop', '0002_auto_20201007_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]
