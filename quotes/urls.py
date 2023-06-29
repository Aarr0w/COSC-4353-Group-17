from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('home/', views.index, name = 'index'),
    path('form/submit/', views.return_quote),   
    path('register/', views.register),
    path('login/', views.login_view, name='login'),   
]
