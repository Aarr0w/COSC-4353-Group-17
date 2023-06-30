from django.db import models
from django.core.validators import MinLengthValidator
States_Choices = (
    ('al','AL'),
    ('ak','AK'),
    ('az','AZ'),
    ('ar','AR'),
    ('as','AS'),
    ('ca','CA'),
    ('co','CO'),
    ('ct','CT'),
    ('de','DE'),
    ('fl','FL'),
    ('ga','GA'),
    ('hi','HI'),
    ('id','ID'),
    ('il','IL'),
    ('in','IN'),
    ('ia','IA'),
    ('ks','KS'),
    ('ky','KY'),
    ('la','LA'),
    ('me','ME'),
    ('md','MD'),
    ('ma','MA'),
    ('mi','MI'),
    ('mn','MN'),
    ('ms','MS'),
    ('mo','MO'),
    ('mt','MT'),
    ('ne','NE'),
    ('nv','NV'),
    ('nh','NH'),
    ('nj','NJ'),
    ('nm','NM'),
    ('ny','NY'),
    ('nc','NC'),
    ('nd','ND'),
    ('oh','OH'),
    ('ok','OK'),
    ('or','OR'),
    ('pa','PA'),
    ('ri','RI'),
    ('sc','SC'),
    ('sd','SD'),
    ('tn','TN'),
    ('tx','TX'),
    ('ut','UT'),
    ('vt','VT'),
    ('va','VA'),
    ('wa','WA'),
    ('wv','WV'),
    ('wi','WI'),
    ('wy','WY'),

)
# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=50)
    Address_1 = models.CharField(max_length=100)
    Address_2 = models.CharField(max_length=100, null = True)
    City = models.CharField(max_length=100)
    #State = models.CharField(max_length=10)
    State = models.CharField(max_length=15, choices= States_Choices, default='tx')
   #State (Drop Down, selection required) DB will store 2 character state code 
    Zipcode = models.CharField(max_length=9,validators=[MinLengthValidator(5,'the field must contain at least 5 characters')]) # how to set min_length?  

    ''' - Full Name (50 characters, required)
        - Address 1 (100 characters, required)
        - Address 2 (100 characters, optional)
        - City (100 characters, required)
        - State (Drop Down, selection required) DB will store 2 character state code
        - Zipcode (9 characters, at least 5 character code required)
    '''
    #class Meta:
     #   constraints = [
      #       models.CheckConstraint(
       #           check=models.Q(Zipcode__length__gte=1)
        #     )
        #]

class Quote(models.Model):
    #user_name = models.CharField(max_length=200)
    gallons_requested = models.DecimalField(decimal_places=2, max_digits = 10, default = 7)
    delivery_address = models.CharField(max_length=200, default = 'Houston')
    delivery_date = models.DateField()
    ''' Date/time	models.DateTimeField()	datetime NOT NULL	
        datetime NOT NULL	timestamp with time zone NOT NULL	
        TIMESTAMP NOT NULL	Creates a datetime field to s'''
    suggested_price = models.DecimalField(decimal_places=2, max_digits = 10, default = 3.09)    
    total_amount_due = models.DecimalField(decimal_places=2, max_digits = 10, default = 50)



