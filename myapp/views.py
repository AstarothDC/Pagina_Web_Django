from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    path = request.path
    response = HttpResponse('This works !')
    return response