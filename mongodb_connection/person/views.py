from django.shortcuts import render

# Create your views here.
from .models import person_collection
from django.http import HttpResponse




def index(request):
    return HttpResponse("<h1> App is running </h1>")



def add_person(request):
    records = {
        "first_name": "Shovan",
        "last_name" : "Paul"
    }
    person_collection.insert_one(records)
    return HttpResponse("New Person Added")

def get_all_person(request):
    persons = person_collection.find()
    return HttpResponse(persons)

