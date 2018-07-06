from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, MATERIALES

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):
	material=MATERIALES(Nombre="Seider",Cantidad=2)
    greeting = Greeting()
    greeting.save()
	material.save
    greetings = Greeting.objects.all()
    materiales=MATERIALES.objects.all()

    return render(request, 'db.html', {'greetings': greetings,'materiales':})

