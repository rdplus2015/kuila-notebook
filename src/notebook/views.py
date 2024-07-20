from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from notebook.models import Note
from utils.mixins import KuilaLoginRequiredMixin


# Create your views here.


class NoteListView(KuilaLoginRequiredMixin, ListView):
    model = Note
    template_name = 'notebook/index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class NotePreview(DetailView):
    model = Note
    template_name = 'notebook/note_preview.html'
    context_object_name = 'note'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk, user=self.request.user)


class NoteCreateView(KuilaLoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notebook/note_form_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class NoteUpdateView(KuilaLoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notebook/note_form_update.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk, user=self.request.user)


class NoteDeleteView(KuilaLoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notebook/note_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk, user=self.request.user)
