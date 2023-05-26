from django.contrib import admin

# Register your models here.

from .models import Category, Car, Booking

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Booking)