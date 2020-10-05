from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy
from userprofile.forms import ItemDescriptionForm
from django.http import HttpResponseForbidden, HttpResponseRedirect


class VacancyList(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy/vacancy_list.html", {"vacancy_list": Vacancy.objects.all()})


class NewVacancy(View):
    def get(self, request, *args, **kwargs):
        form = ItemDescriptionForm()
        return render(request, 'vacancy/vacancy_new.html', {'description_form': form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden()
        form = ItemDescriptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['description']  # data is a regular dictionary
            name = request.user
            Vacancy.objects.create(description=data, author=name)
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'vacancy/vacancy_new.html', {'description_form': form})