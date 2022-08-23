
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('sumar/',views.sumar, name="suma"),
   path('restar/',views.restar, name="resta"),
   path('multiplicar/',views.multiplicar, name="multiplica"),
   path('dividir/',views.dividir, name="divide"),
]
