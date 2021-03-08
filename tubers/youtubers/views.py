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
    tubers = Youtuber.objects.order_by('-created_date')

    city_search = Youtuber.objects.values_list('city',flat='True').distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat='True').distinct()
    category_search = Youtuber.objects.values_list('category',flat='True').distinct()



    keyword = request.GET.get('keyword',None)
    if keyword:
        tubers = tubers.filter(description__icontains=keyword)

    city = request.GET.get('city',None)
    if city:
        tubers = tubers.filter(city__iexact=city)
    
    camera_type = request.GET.get('camera_type',None)
    if camera_type:
        tubers = tubers.filter(camera_type__iexact=camera_type)

    category = request.GET.get('category',None)
    if category:
        tubers = tubers.filter(category__iexact=category)

    data = {
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search,
    }
    return render(request, 'youtubers/search.html',data)

