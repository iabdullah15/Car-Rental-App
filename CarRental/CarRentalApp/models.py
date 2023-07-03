from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    objects = CustomUserManager()


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


class Car(models.Model):
    car_name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default = 80.00)
    category = models.ForeignKey(Category, models.CASCADE)
    car_image = models.ImageField(null = True, blank = True, upload_to="images/")

    def __str__(self) -> str:
        return self.car_name + " " + self.category.category_name


class Booking(models.Model):
    # customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    booking_date = models.DateField()
    return_date = models.DateField()


class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, 
                             validators=[RegexValidator(
                                 regex=r'^\d{11}$',
                                 message="Contact number must be exactly 11 digits."
                             )])
    subject = models.CharField(max_length=50, default="")
    message = models.TextField()

    def __str__(self) -> str:
        return self.subject