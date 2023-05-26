from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView

from .models import Booking, Car, Category

# Create your views here.

# class HomeListView(ListView):

#     model = Car
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):

#         context = super().get_context_data(**kwargs)
#         context['economy'] = Car.objects.filter(category__category_name= 'Economy')
#         context['sports'] = Car.objects.filter(category__category_name = 'Sports')
#         context['luxury'] = Car.objects.filter(category__category_name = 'Luxury')
#         context['suv'] = Car.objects.select_related('category').filter(category__category_name = 'SUV')

#         print(context)
#         return context

class Home(View):


    def get(self, request):

        economy = Car.objects.filter(category__category_name= 'Economy')[:4]
        sports = Car.objects.filter(category__category_name = 'Sports')
        luxury = Car.objects.filter(category__category_name = 'Luxury')
        suv = Car.objects.select_related('category').filter(category__category_name = 'SUV')

        context = {
            'economy': economy, 
            'sports': sports,
            'luxury': luxury,
            'suv': suv
        }

        return render(request, 'index.html', context)
    

class CarListView(ListView):

    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'


class EconomyListView(ListView):

    model = Car
    template_name = 'economy-cars.html'
    context_object_name = 'economy'

    def get_queryset(self) -> QuerySet[Any]:
        
        return Car.objects.filter(category__category_name = 'Economy')


class SportsListView(ListView):

    model = Car
    template_name = 'sports-cars.html'
    context_object_name = 'sports'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(category__category_name = 'Sports')
    

class SUVListView(ListView):

    model = Car
    template_name = 'suv-cars.html'
    context_object_name = 'suv'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(category__category_name = 'SUV')
    

class LuxuryListView(ListView):

    model = Car
    template_name = 'luxury-cars.html'
    context_object_name = 'luxury'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(category__category_name = 'Luxury')
    