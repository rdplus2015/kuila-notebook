from django.views.generic import TemplateView

from utils.mixins import KuilaLoginRequiredMixin


class Home(TemplateView):
    template_name = 'index.html'



class SettingsView(KuilaLoginRequiredMixin,TemplateView):
    template_name = 'notebook/settings.html'


