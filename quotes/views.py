from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from .forms import CustomerForm, FuelRequestForm, LoginRegistration


def calculate(a,b,c):
    x = 1
    y = 2
    return str(a+b+c)


def index(request):
    return render(request, 'base.html', {})
    
def home(request):
    return render(request, "welcome.html",{})

def profile(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'customer_form.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password )
        if user is not None:
            login(request, user)
            return redirect('ho')
        else:
            pass
    return render(request, 'login.html')
def login_register(request):
    form = LoginRegistration()
    if request.method == 'POST':
        form = LoginRegistration(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'login_reg.html', context)

def fuel_request(request):
    
    form = FuelRequestForm()
    if request.method == 'POST':
        form = FuelRequestForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'fuel_request.html', context)

def return_quote(request):
    num = calculate(1,5,7)
    return render(request, 'show_quote.html', {'quote':num})
