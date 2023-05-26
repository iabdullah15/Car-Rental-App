from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


class Car(models.Model):
    car_name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default = 80.00)
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self) -> str:
        return self.car_name +" " + self.category.category_name


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    booking_date = models.DateField()
    return_date = models.DateField()