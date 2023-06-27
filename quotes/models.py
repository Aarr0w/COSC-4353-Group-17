from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=50)
    Address_1 = models.CharField(max_length=100)
    Address_2 = models.CharField(max_length=100, null = True)
    City = models.CharField(max_length=100)
   #State (Drop Down, selection required) DB will store 2 character state code 
    Zipcode = models.CharField(max_length=9) # how to set min_length?  

    ''' - Full Name (50 characters, required)
        - Address 1 (100 characters, required)
        - Address 2 (100 characters, optional)
        - City (100 characters, required)
        - State (Drop Down, selection required) DB will store 2 character state code
        - Zipcode (9 characters, at least 5 character code required)
    '''


class Quote(models.Model):
    user_name = models.CharField(max_length=200)
    date = models.DateTimeField(max_length=200)
    ''' Date/time	models.DateTimeField()	datetime NOT NULL	
        datetime NOT NULL	timestamp with time zone NOT NULL	
        TIMESTAMP NOT NULL	Creates a datetime field to s'''
    delivery_address = models.CharField(max_length=200, default = 'Houston')
    gallons_requested = models.DecimalField(decimal_places=2, max_digits = 10, default = 7)
    profit_margin = models.DecimalField(decimal_places=2, max_digits = 10, default = 0.2)
    quote_amount = models.DecimalField(decimal_places=2, max_digits = 10, default = 100)



