from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import request
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context)


    
