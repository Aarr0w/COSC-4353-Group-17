# import the standard Django Model
# from built-in library
from django.db import models
from django import forms
from .models import User
from .models import Quote

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
        fields = "__all__"
        widgets = {
            'delivery_date': DateInput(),
        }
        #exclude = ['date_created', 'quote_amount']
