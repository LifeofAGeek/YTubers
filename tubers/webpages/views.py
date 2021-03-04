from django.shortcuts import render
from .models import Slider, team
from youtubers.models import Youtuber
# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    teams = team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.all()
    data={
        'sliders': sliders,
        'teams' : teams,
        'featured_youtubers' : featured_youtubers,
        'all_youtubers' : all_youtubers,
    }
    return render(request,'webpages/home.html',data)

def services(request):
    return render(request,'webpages/services.html')

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')