# Generated by Django 4.1.7 on 2023-05-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalApp', '0004_car_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
