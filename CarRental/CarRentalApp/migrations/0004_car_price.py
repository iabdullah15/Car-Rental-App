# Generated by Django 4.1.7 on 2023-03-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalApp', '0003_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=80.0, max_digits=5),
        ),
    ]
