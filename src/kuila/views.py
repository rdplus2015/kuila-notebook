from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'notebook/index.html'


@method_decorator(login_required, name='dispatch')
class SettingsView(TemplateView):
    template_name = 'notebook/settings.html'


