from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import HttpRequest
from .forms import CustomerForm, FuelRequestForm, LoginRegistration, FuelRequestHistory, ProfileForm
from .models import Quote, Profile
from django.contrib.auth.decorators import login_required


def calculate(state, history, gallons):
    currentPrice = 1.50
    # Suggested Price = Current Price (1.50) + Margin
    # Margin = Current Price * (Location Factor - Rate History Factor + Gallons Requested Factor + Company Profit Factor)

    # Company Profit Factor = 0.1
    # Location Factor: Texas = 0.02 ; Other = 0.04
    # Rate History Factor: History = 0.01 ; Other - 0.00
    # Gallons Requested Factor: <= 1000 = 0.03 ; > 1000 = 0.02

    # Total Price = Suggested Price * Gallons

    profitFactor = 0.10

    # Location Factor
    # state = state.upper()  # for consistency
    if state == 'TX':
        locationFactor = 0.02
    else:
        locationFactor = 0.04

    # Rate History Factor
    if history == 1:
        historyFactor = 0.01
    else:
        historyFactor = 0.00

    # Gallons Requested Factor
    if gallons > 1000:
        gallonsFactor = 0.02
    else:
        gallonsFactor = 0.03

    # Margin Calculation
    margin = currentPrice * \
        (locationFactor - historyFactor + gallonsFactor + profitFactor)
    suggestedPrice = currentPrice + margin
    totalDue = gallons * suggestedPrice
    totalDue = "%.2f" % totalDue

    return totalDue
    
def index(request):
    return render(request, 'base.html', {})
    
def home(request):
    return render(request, "welcome.html",{})

def profile(request):
    #form = CustomerForm()
    form = ProfileForm()
    if request.method == 'POST':
        #form = CustomerForm(request.POST)
        form  = ProfileForm(request.POST)
        username = request.session.get('username')
        if form.is_valid() and username:
            instance = form.save(commit=False)
            instance.username = username        
            instance.save()
        else:
            messages.info(request, 'Must be logged in to edit profile')
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
            print('============================================================')
            print('gallons requested: ' + str(instance.gallons_requested))
            total_due = return_quote(request, instance.gallons_requested)
  
            print('total due:' + str(total_due))
          
            instance.total_amount_due = total_due
            instance.save()
            return  render(request, 'show_quote.html', {'amount':total_due})
        else:
            messages.info(request, 'Must be logged in to view Request History')
    context = {'form': form}
    #return render(request, 'fuel_request.html', context)
    return render(request, 'fuel_request.html', context)
    

def fuel_history(request):
    username = request.session.get('username')
    if username:
        user_data = Quote.objects.filter(username=username)
        context = {'user_data': user_data}
        return render(request, 'fuel_request_history.html',context)
    else:
       return render(request, 'fuel_request_history.html') 
   
def return_quote(request, gallons_requested):
    #user_state = User.objects.filter(username = request.session.get('username')).values('quote_amount')
    user_history = Quote.objects.filter(username = request.session.get('username')).all()
    user_state = Profile.objects.filter(username = request.session.get('username')).values('State')[0]
    if len(user_history) > 0:
        history = 1
    else:
        history = 0
    
    if not user_state:
        user_state = 'TX'
    print('============================================================')
    print('user_state: ' + str(user_state))
    #num = calculate('tx', history, float(gallons_requested) ) #Parameters need to be changed to be dynamic with current request form
    num = calculate(user_state, history, float(gallons_requested) ) #Parameters need to be changed to be dynamic with current request form
    return num
    #(State, History (1 if there is a previous quote or 0 otherwise), number of gallons requested)
    #return render(request, 'show_quote.html', {'amount':num})
    #return 
