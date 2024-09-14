from django.views.generic import TemplateView
from categories.views import CategoryListView
from kuila.mixins import KuilaLoginRequiredMixin
from notebook.views import NoteListView

# Defines a view for the home page that uses the 'index.html' template.
class Home(TemplateView):
    template_name = 'index.html'  # Specifies the template for rendering the home page


# Defines a view for the dashboard, which requires the user to be logged in.
# It uses the 'main/dashboard.html' template.
class Dashboard(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'main/dashboard.html'  # Specifies the template for the dashboard view


# Defines a view for the settings page that requires the user to be logged in.
# It uses the 'main/settings.html' template.
class SettingsView(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'main/settings.html'  # Specifies the template for rendering the settings page
