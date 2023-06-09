from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('cars/', views.CarListView.as_view(), name = 'cars'),
    path('cars/economy', views.EconomyListView.as_view(), name='economy_cars'),
    path('cars/sports', views.SportsListView.as_view(), name='sports_cars'),
    path('cars/suv', views.SUVListView.as_view(), name = 'suv_cars'),
    path('cars/luxury', views.LuxuryListView.as_view(), name='luxury_cars'),
    path('login', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login_view'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('cars/search', views.car_search, name='car_search'),

]