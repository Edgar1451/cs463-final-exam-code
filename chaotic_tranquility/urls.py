"""chaotic_tranquility URL Configuration
"""
from django.contrib import admin
from django.urls import path

from chaos_app.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('person/<int:pk>/', PersonalNetView.as_view(), name='person'),
]
