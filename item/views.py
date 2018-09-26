from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Asset
from .import views
from django.contrib.auth.models import User
# Create your views here.
# @login_required
def homepage(request):
	assets = Asset.objects.all()
	return render(request, 'homepage.html',{'assets': assets})

@login_required
def asset_list(request):
	assets = Asset.objects.all()
	return render(request, 'asset_list.html', {'assets':assets})

def list(request):
	return render(request, 'list.html')