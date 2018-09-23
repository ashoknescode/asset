from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
#     url(r'^login/', views.loginview, name='loginview'),
#     url(r'^logout/', views.logoutview, name='logoutview'),
]
