# Generated by Django 4.2.1 on 2023-05-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
