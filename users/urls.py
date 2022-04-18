from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('account/login', views.LoginView.as_view(), name='login'),
    path('account/logout', views.LogoutView.as_view(), name='logout'),
]
