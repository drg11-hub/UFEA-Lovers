"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Contact_us',views.Contact_us, name='Contact_us'),
    path('About_us',views.About_us, name='About_us'),
    path('Profile', views.userProfile, name='userProfile'),
    path('Signup', views.handleSignup, name='handleSignup'),
    path('Login', views.log_in, name='log_in'),
    path('Logout', views.log_out, name='log_out'),
]
