from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview'),
]
