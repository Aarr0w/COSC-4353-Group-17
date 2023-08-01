# import the standard Django Model
# from built-in library
from typing import Any, Dict
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
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
def DateVal(x):
     
     return x
class FuelRequestForm(forms.ModelForm): 
    class Meta:
        model = Quote
        fields = ['gallons_requested', 'delivery_address', 'delivery_date']
        widgets = {
            'delivery_date': DateInput()
        }
    def clean_delivery_date(self):
         data = self.cleaned_data['delivery_date']
         current_date = timezone.now().date()

         if data < current_date:
              raise forms.ValidationError("Please select a date in the future.")
         return data
 
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
          
          