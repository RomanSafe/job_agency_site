from django.shortcuts import render
from django.views import View
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.views.generic import CreateView
# from django.contrib.auth.views import LoginView
# from django import forms


class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainpage/base.html')
