from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# resquest -> handler

def say_hello(request):

    return render(request,'hello.html')