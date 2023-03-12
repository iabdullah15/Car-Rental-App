from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)


class Car(models.Model):
    car_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.CASCADE)


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    booking_date = models.DateField()
    return_date = models.DateField()