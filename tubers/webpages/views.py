from django.shortcuts import render
from .models import Slider, team

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = team.objects.all()
    data={
        'sliders': sliders,
        'teams' : teams
    }
    return render(request,'webpages/home.html',data)

def services(request):
    return render(request,'webpages/services.html')

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')