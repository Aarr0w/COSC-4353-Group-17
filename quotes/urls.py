from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index, name = 'home'),
    path('form/submit/', views.return_quote),   
    path('register/', views.register, name = 'register'),
    path('profile/', views.register, name = 'profile'),
    path('fuel_request/', views.fuel_request, name = 'fuel_request'),
    path('login/', views.login_view, name='login')   
]
