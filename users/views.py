from django.shortcuts import render
from django.contrib.auth.views import LoginView


class LoginView(LoginView):
    template_name = 'login.html'