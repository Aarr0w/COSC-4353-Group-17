from django.test import TestCase, Client, SimpleTestCase
from quotes.models import Profile, Quote
from .forms import FuelRequestForm, ProfileForm

class ModelsTestClass(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_profile1 = Profile.objects.create(username="Pwright",firstname="Phoenix",lastname="Wright",Address_1="ABCDE",City="Houston",State="TX",Zipcode="70000")
        test_profile1.save()

        test_quote1 = Quote.objects.create(username="Pwright",gallons_requested = '7',delivery_address="Houston",suggested_price= "10",total_amount_due="70")
        test_quote1.save()
        pass

    def setUp(self):
        self.client = Client()

    def test_quote_form(self):                                      #Checks if the quote form is valid
        form = FuelRequestForm(data={'username': "Pwright",'gallons_requested' : '7','delivery_address':"Houston",'suggested_price': "10",'total_amount_due':"70"})
        self.assertTrue(form.is_valid)

    def test_profile_form(self):
        form = ProfileForm(data={'username':"Pwright",'firstname':"Phoenix",'lastname':"Wright",'Address_1':"ABCDE",'City':"Houston",'State':"TX",'Zipcode':"70000"})
        self.assertTrue(form.is_valid)
    
    def test_profile(self):     
        test_profile1 = Profile.objects.get(username="Pwright")
        self.assertTrue(len(test_profile1.firstname)>0)            #Assertion to check if firstname exists
        self.assertTrue(len(test_profile1.lastname)>0)             #Assertion to check if lastname exists
        self.assertTrue(len(test_profile1.Address_1)>0)            #Assertion to check if Address line 1 exists. Line 2 is not required
        self.assertTrue(len(test_profile1.City)>0)                 #Assertion to check if city exists
        self.assertTrue(5<=len(test_profile1.Zipcode)<=9)          #Assertion to check zipcode length is between 5 and 9 digits
    
    def test_quote(self):
        test_quote1 = Quote.objects.get(username="Pwright")
        self.assertTrue(test_quote1.gallons_requested > 0)          #Assertion to check if gallons requested is more than 0

