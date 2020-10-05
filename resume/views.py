from django.shortcuts import render
from django.views import View
from resume.models import Resume
from userprofile.forms import ItemDescriptionForm
from django.http import HttpResponseForbidden, HttpResponseRedirect


class ResumeList(View):
    def get(self, request, *args, **kwargs):
        return render(request, "resume/resume_list.html", {"resume_list": Resume.objects.all()})


class NewResume(View):
    def get(self, request, *args, **kwargs):
        form = ItemDescriptionForm()
        return render(request, 'resume/resume_new.html', {'description_form': form})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_staff:
            return HttpResponseForbidden()
        form = ItemDescriptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['description']  # data is a regular dictionary
            name = request.user
            Resume.objects.create(description=data, author=name)
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'resume/resume_new.html', {'description_form': form})
