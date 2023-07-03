from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Booking, Car, Category, CustomUser, Contact
from .forms import CustomUserCreationForm, ContactForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def success(request:HttpRequest):

    if request.method == 'GET':
        messages.success(request, 'Form submitted succesfully.')
        return render(request, 'success.html', {})
    
    else:
        return redirect(reverse_lazy('home'))



def car_search(request:HttpRequest):

    if request.method == 'GET':

        searched = request.GET.get('search')
        print(searched)
        cars = None

        if searched:
            cars = Car.objects.filter(car_name__icontains = searched)
        else:
            cars = None

        return render(request, 'searched-cars.html', {'searched':cars})
        

class ContactView(CreateView):

    # model = Contact
    form_class = ContactForm
    template_name = 'contact-form.html'
    context_object_name = 'form'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
    

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted succesfully.')

        return redirect(reverse_lazy('success_page'))



class Register(CreateView):
    
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login_view')
    template_name = 'accounts/register.html'



class Home(View):

    def get(self, request:HttpRequest):

        economy = Car.objects.filter(category__category_name= 'Economy').order_by('?')[:4]
        sports = Car.objects.filter(category__category_name = 'Sports').order_by('?')[:4]
        luxury = Car.objects.filter(category__category_name = 'Luxury').order_by('?')[:4]
        suv = Car.objects.select_related('category').filter(category__category_name = 'SUV').order_by('?')[:4]

        context = {
            'economy': economy, 
            'sports': sports,
            'luxury': luxury,
            'suv': suv
        }

        return render(request, 'index.html', context)
    
    

class CarListView(LoginRequiredMixin, ListView):

    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.all().order_by('?')


class EconomyListView(LoginRequiredMixin, ListView):

    # paginate_by = 2
    model = Car
    template_name = 'economy-cars.html'
    context_object_name = 'economy'

    def get_queryset(self) -> QuerySet[Any]:
        
        return Car.objects.filter(category__category_name = 'Economy')


class SportsListView(LoginRequiredMixin, ListView):

    model = Car
    template_name = 'sports-cars.html'
    context_object_name = 'sports'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(category__category_name = 'Sports')
    

class SUVListView(LoginRequiredMixin, ListView):

    model = Car
    template_name = 'suv-cars.html'
    context_object_name = 'suv'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(category__category_name = 'SUV')
    

class LuxuryListView(LoginRequiredMixin, ListView):

    model = Car
    template_name = 'luxury-cars.html'
    context_object_name = 'luxury'

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(category__category_name = 'Luxury')


class EconomyDetailView(LoginRequiredMixin, DetailView):

    model = Car
    template_name = 'economy-detail.html'
    pk_url_kwarg = 'car_id'     #Name of the url parameter defined in urls.py

    def get_object(self, queryset=None):
        id = self.kwargs.get('car_id')
        car = get_object_or_404(Car, id=id, category__category_name="Economy")
        return car
    

class LuxuryDetailView(LoginRequiredMixin, DetailView):

    model = Car
    template_name = 'luxury-detail.html'
    pk_url_kwarg = 'car_id'     #Name of the url parameter defined in urls.py

    def get_object(self, queryset=None):
        id = self.kwargs.get('car_id')
        car = get_object_or_404(Car, id=id, category__category_name="Luxury")
        return car