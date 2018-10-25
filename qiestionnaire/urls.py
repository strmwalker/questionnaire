"""qiestionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app.forms import NameForm, LookForm, AnimalForm
from app.views import RespondentWizard, RespondentListView, RespondentView
from qiestionnaire import settings

named_respondent_forms = (
    ('name', NameForm),
    ('look', LookForm),
    ('pets', AnimalForm)
)

respondent_wizard = RespondentWizard.as_view(
    named_respondent_forms,
    url_name='questionnaire_step',
    done_step_name='thank-you')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('questionnaire/<str:step>/', respondent_wizard, name='questionnaire_step'),
    path('questionnaire/', respondent_wizard, name='questionnaire'),
    path('thank-you/', TemplateView.as_view(template_name='thank_you.html')),
    path('respondents/', RespondentListView.as_view(), name='view_respondents'),
    path('respondents/<int:pk>/', RespondentView.as_view(), name='view_respondent')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
