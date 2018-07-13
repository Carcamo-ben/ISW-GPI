from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def profile(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'profile.html')
def helper(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'helper.html')
def solicitudes(request):
    if request.method == 'POST':
        form=SOLICITUDESForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/helper/')
    return render(request, 'solicitudes.html',{'form':SOLICITUDESForm()})