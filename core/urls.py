from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AdministrationHomePageView.as_view(), name='homepage'),
]
