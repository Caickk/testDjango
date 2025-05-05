from django.urls import path
from . import views

#Configuração de URL
urlpatterns = [
    path('hello/',views.say_hello)
]