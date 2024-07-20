from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from utils.mixins import KuilaLoginRequiredMixin


class Home(TemplateView):
    template_name = 'index.html'


class Dashboard(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'notebook/index.html'


class SettingsView(KuilaLoginRequiredMixin,TemplateView):
    template_name = 'notebook/settings.html'


