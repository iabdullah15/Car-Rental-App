from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cars/', views.CarListView.as_view(), name = 'cars'),
    path('cars/economy', views.EconomyListView.as_view(), name='economy_cars'),
    path('cars/sports', views.SportsListView.as_view(), name='sports_cars'),
    path('cars/suv', views.SUVListView.as_view(), name = 'suv_cars'),
    path('cars/luxury', views.LuxuryListView.as_view(), name='luxury_cars')
]