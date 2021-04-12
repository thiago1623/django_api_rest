from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from persons.models import Person

def home(request):
    persons = Person.objects.all()
    return HttpResponse(persons)