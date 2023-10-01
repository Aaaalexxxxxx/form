from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.urls import reverse

# Create your views here.
#запросы на отображение страниц

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_adv/index.html', context)

def top_sellers(request):
    return render(request, 'app_adv/top-sellers.html')

def advertisement_post(request):
    if request.method =='POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user 
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
        else:
            context = {'form': form}
            return render(request, 'app_adv/advertisement-post.html', context) 
    else:
        form = AdvertisementForm()
        
        
