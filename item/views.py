from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Asset
from .import views
# Create your views here.

def homepage(request):
	assets = Asset.objects.all()
	return render(request, 'homepage.html',{'assets': assets})

@login_required

def asset_list(request):
	assets = Asset.objects.all()
	return render(request, 'asset_list.html', {'assets':assets})

def login(request):
	return render(request, 'login.html')