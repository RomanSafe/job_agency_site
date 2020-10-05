"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from mainpage.views import MainPage
from userprofile.views import LogIn, SignUp, Profile
from vacancy.views import VacancyList, NewVacancy
from resume.views import ResumeList, NewResume
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView


urlpatterns = [
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home/', RedirectView.as_view(url='/home')),
    path('resume/new/', RedirectView.as_view(url='/resume/new')),
    path('vacancy/new/', RedirectView.as_view(url='/vacancy/new')),
    path('home', Profile.as_view()),
    path('resume/new', NewResume.as_view()),
    path('vacancy/new', NewVacancy.as_view()),
    path('admin/', admin.site.urls),
    path("vacancies/", VacancyList.as_view()),
    path("resumes/", ResumeList.as_view()),
    path('login', LogIn.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', SignUp.as_view()),
    path('', MainPage.as_view()),
]
