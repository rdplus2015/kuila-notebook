
from django.views.generic import TemplateView
from categories.views import CategoryListView
from kuila.mixins import KuilaLoginRequiredMixin
from notebook.views import NoteListView


class Home(TemplateView):
    template_name = 'index.html'


class Dashboard(KuilaLoginRequiredMixin, TemplateView):
    template_name = 'main/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add categories context
        category_view = CategoryListView()
        category_view.request = self.request
        context['categories'] = category_view.get_queryset()

        # Add notes context
        note_view = NoteListView()
        note_view.request = self.request
        context['notes'] = note_view.get_queryset()
        return context


class SettingsView(KuilaLoginRequiredMixin,TemplateView):
    template_name = 'main/settings.html'

