from django.http import HttpResponse
from django.shortcuts import render
from .import views
# Create your views here.

def homepage(request):
	return render(request, 'homepage.html')