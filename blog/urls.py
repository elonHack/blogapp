
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post>', views.detailed_post, name='single_post')
]
