from django.conf.urls import path,include
from django.contrib import admin

from .import views

app_name = 'item'

urlpatterns = [
	
	path('item/', views.home, name='hompage'),
	path('item/', views.asset_list, name="list")
	]