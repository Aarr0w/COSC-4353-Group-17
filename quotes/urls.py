from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.home, name = 'home'),
    path('form/submit/', views.return_quote),   
    path('profile/', views.profile, name = 'profile'),
    path('fuel_request/', views.fuel_request, name = 'fuel_request'),
    path('login/', views.login_view, name='login'), 
    path('login/registration',views.login_register , name ='register' )  
]
