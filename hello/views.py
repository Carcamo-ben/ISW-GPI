from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def profile(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'profile.html')
    
def solicitudes(request):
    form=SOLICITUDESForm()
    return render(request, 'solicitudes.html',{'form':form})