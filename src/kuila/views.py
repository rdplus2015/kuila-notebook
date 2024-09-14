from django.views.generic import TemplateView
from categories.views import CategoryListView
from kuila.mixins import KuilaLoginRequiredMixin
from notebook.views import NoteListView

# Defines a view for the home page that uses the 'index.html' template.


class Home(TemplateView):
    template_name = 'index.html'


class Dashboard(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'main/dashboard.html'





"""
# Defines a view for the dashboard page that requires the user to be logged in.
# It uses the 'main/dashboard.html' template and adds context data for categories and notes.

class Dashboard(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'main/dashboard.html'

    # Adds context data to the template, including categories and notes.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Create an instance of CategoryListView, set the request, and get the queryset to add to context.
        category_view = CategoryListView()
        category_view.request = self.request
        context['categories'] = category_view.get_queryset()

        # Create an instance of NoteListView, set the request, and get the queryset to add to context.
        note_view = NoteListView()
        note_view.request = self.request
        context['notes'] = note_view.get_queryset()
        return context
"""



# Defines a view for the settings page that requires the user to be logged in.
# It uses the 'main/settings.html' template.


class SettingsView(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'main/settings.html'
