from django.shortcuts import render
from django.http import HttpRequest
from .forms import CustomerForm

def calculate(a,b,c):
    x = 1
    y = 2
    return str(a+b+c)


def index(request):
    return render(request, 'welcome.html', {'name':'Mr.Krabs'})

def register(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'customer_form.html', context)


def return_quote(request):
    num = calculate(1,5,7)
    return render(request, 'show_quote.html', {'quote':num})