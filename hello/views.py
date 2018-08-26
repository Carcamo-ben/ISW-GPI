from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')
def profile(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'profile.html')
def Succes(request):
    return render(request,'Succes.html')
def helper(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form=HELPERForm(request.POST)
        #HELPERForm.Solicitud=SOLICITUDES.objects.all().order_by('-id')[0]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./Succes/')
    return render(request, 'helper.html',{'form':HELPERForm()})
def solicitudes(request):
    if request.method == 'POST':
        form=SOLICITUDESForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./helper/')
    return render(request, 'solicitudes.html',{'form':SOLICITUDESForm()})