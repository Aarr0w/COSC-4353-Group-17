# import the standard Django Model
# from built-in library
from django.db import models
from django import forms
from .models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        #exclude = ['date_created','quote_amount']