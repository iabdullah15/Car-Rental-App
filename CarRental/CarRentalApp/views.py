from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.

def home(request:HttpRequest):

    return render(request, 'home.html')