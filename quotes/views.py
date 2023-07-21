from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import HttpRequest
from .forms import CustomerForm, FuelRequestForm, LoginRegistration, FuelRequestHistory
from .models import Quote
from django.contrib.auth.decorators import login_required

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            request.session['username'] = username
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
    
def login_register(request):
    form = LoginRegistration()
    if request.method == 'POST':    
        form = LoginRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'login_reg.html', context)

def fuel_request(request):   
    form = FuelRequestForm()
    if request.method == 'POST':
        form = FuelRequestForm(request.POST)
        username = request.session.get('username')

        if form.is_valid() and username:
            instance = form.save(commit=False)
            instance.username = username
            instance.save()
            return redirect('fuel_history')
        else:
            messages.info(request, 'Must be logged in to view Request History')
    context = {'form': form}
    return render(request, 'fuel_request.html', context)
    

def fuel_history(request):
    username = request.session.get('username')
    if username:
        user_data = Quote.objects.filter(username=username)
        context = {'user_data': user_data}
        return render(request, 'fuel_request_history.html',context)
    else:
       return render(request, 'fuel_request_history.html') 
   
def return_quote(request):
    num = calculate(1,5,7)
    return render(request, 'show_quote.html', {'quote':num})
