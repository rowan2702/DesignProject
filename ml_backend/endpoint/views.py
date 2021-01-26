
from django.shortcuts import render
from .models import Director, Producer, Narrative, Hero, Actor, Song

# Create your views here.

def home(request) :
    context = { 
        'directors' : Director.objects.all(),
        'producers' : Producer.objects.all(),
        'narratives' : Narrative.objects.all(),
        'heroes' : Hero.objects.all(),
        'actors' : Actor.objects.all(),
        'songs' : Song.objects.all()
    }
    return render(request,'index.html',context)
