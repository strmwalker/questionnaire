import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.generic import ListView
from formtools.wizard.views import NamedUrlSessionWizardView

from app.models import Respondent
from qiestionnaire import settings


def save_data(form_dict):
    resp_dict = {}

    for form in form_dict.values():
        if form.is_valid():
            data = form.cleaned_data
        resp_dict.update(**data)
    respondent = Respondent(**resp_dict)
    respondent.save()


class RespondentWizard(NamedUrlSessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

    def done(self, form_list, form_dict, **kwargs):
        save_data(form_dict)
        return HttpResponseRedirect('/thank-you/')


class RespondentListView(ListView):
    template_name = 'respondent_list.html'
    model = Respondent


class RespondentView(View):

    def get(self, request, pk):
        respondent = Respondent.objects.get(id=pk)
        return render(request, 'respondent_detail.html', context={'object': respondent})

