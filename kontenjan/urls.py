from django.contrib import admin
from django.urls import path
from . import views


app_name= "kontenjan"



urlpatterns = [
    path('kontenjan/', views.kontenjan,name= "kontenjan"), 
    path('ebe21/', views.ebe21,name= "ebe21"), 
    path('hemsire21/', views.hemsire21,name= "hemsire21"), 
]
