from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token, name='token_obtain'),
    path('', include('users.urls')),  
]

""""
1. include all the urls of user and set it defult ' ' mean  server load it's come first 

2. define users and rest_framework,rest_framework_cache, rest_framework.authtoken  
   in INSTALLED_APPS of settings.py

"""
