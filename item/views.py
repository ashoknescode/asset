from django.http import HttpResponse
from django.shortcuts import render
from .models import Asset
from .import views
# Create your views here.

def homepage(request):
	return render(request, 'homepage.html',{'homepage': homepage})

def asset_list(request):
	assets = Asset.objects.all().order_by('date')
	return render(request, 'asset_list.html', {'assets':assets})