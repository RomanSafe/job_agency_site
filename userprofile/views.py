from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from userprofile.forms import ItemDescriptionForm
from django.http import HttpResponseForbidden, HttpResponseRedirect
from resume.models import Resume
from vacancy.models import Vacancy


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'userprofile/signup.html'


class LogIn(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'userprofile/login.html'


class Profile(View):
    def get(self, request, *args, **kwargs):
        form = ItemDescriptionForm()
        return render(request, 'userprofile/profile.html', {'description_form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = ItemDescriptionForm(request.POST)
            if request.user.is_staff:
                model = Vacancy
            else:
                model = Resume
            if form.is_valid():
                data = form.cleaned_data['description']  # data is a regular dictionary
                name = request.user
                model.objects.create(description=data, author=name)
                form = ItemDescriptionForm()
                return render(request, 'userprofile/profile.html', {'description_form': form})
            else:
                return render(request, 'userprofile/profile.html', {'description_form': form})
        else:
            return HttpResponseForbidden()
