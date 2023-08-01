# import the standard Django Model
# from built-in library
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Quote,Register, Profile


class DateInput(forms.DateInput):
        input_type = 'date'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        
        #exclude = ['date_created','quote_amount']

class FuelRequestForm(forms.ModelForm): 
    class Meta:
        model = Quote
        fields = ['gallons_requested', 'delivery_address', 'delivery_date']
        widgets = {
            'delivery_date': DateInput()
        }
 
class LoginRegistration(UserCreationForm):
     class Meta:
        model = User
        fields = ['username','password1','password2']

class FuelRequestHistory(forms.ModelForm):
     class Meta:
          model = Quote
          fields = "__all__"
       

class ProfileForm(forms.ModelForm):
     class Meta:
          model = Profile
          fields = ['firstname', 'lastname', 'Address_1','Address_2', 'City', 'State', 'Zipcode']
          
          