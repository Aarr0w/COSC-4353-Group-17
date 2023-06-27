from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index, name = 'index'),
    path('form/submit/', views.return_quote),   
    path('register/', views.register)   
]
