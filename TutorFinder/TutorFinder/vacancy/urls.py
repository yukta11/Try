
from django.contrib import admin
from django.urls import path, include
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('vacancyform/', views.vacancyform, name='vacancyform'),
    path('home/', views.home, name='home'),
]
