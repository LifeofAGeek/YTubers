from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_object_or_404
# Create your views here.

 
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers' : tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request,id):
    tubers = get_object_or_404(Youtuber, pk=id)
    data = {
        'tubers' : tubers,
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    pass

