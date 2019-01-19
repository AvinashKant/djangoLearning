from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
# name='details' same as route in laravel
 

    path('a', views.rendermethod,name='details'),
     path('show', views.firstaa,name='aa'),
     path('/ba', views.first,name='first'),
    #path('/b', views.index2),
]