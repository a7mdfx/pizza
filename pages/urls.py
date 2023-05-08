import django.urls 
from django.urls import path
from . import views

urlpatterns =[
    path('home', views.all_pizzas,name ='index'),
]