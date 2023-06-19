from .models import Booking, CustomUser
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms.widgets import DateInput

class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):

    date_of_birth = forms.DateField(widget=DateInput(attrs={'type':'date'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'city', 'id_number')
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'city')