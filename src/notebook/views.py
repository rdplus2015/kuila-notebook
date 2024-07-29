from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from categories.models import Category
from notebook.models import Note
from kuila.mixins import KuilaLoginRequiredMixin


# View for listing notes, restricted to logged-in users
class NoteListView(KuilaLoginRequiredMixin, ListView):
    model = Note  # Model to be used for the view
    template_name = 'note/index.html'  # Template to render
    context_object_name = 'notes'  # Context variable name for the list of notes

    def get_queryset(self):
        # Return notes that belong to the current user
        return Note.objects.filter(user=self.request.user)


# View for previewing a single note, restricted to logged-in users
class NotePreview(KuilaLoginRequiredMixin, DetailView):
    model = Note  # Model to be used for the view
    template_name = 'note/note_preview.html'  # Template to render
    context_object_name = 'note'  # Context variable name for the note

    def get_object(self, queryset=None):
        # Get the note object by primary key and ensure it belongs to the current user
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk, user=self.request.user)


# View for creating a new note, restricted to logged-in users
class NoteCreateView(KuilaLoginRequiredMixin, CreateView):
    model = Note  # Model to be used for the view
    template_name = 'note/note_form_create.html'  # Template to render
    fields = ['title', 'content', 'category']  # Fields to include in the form
    success_url = reverse_lazy('dashboard')  # Redirect URL after successful form submission

    def get_form(self, form_class=None):
        # Filter the category choices to only those belonging to the current user
        form = super().get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        # Set the user of the note to the current user
        form.instance.user = self.request.user
        return super().form_valid(form)


# View for updating an existing note, restricted to logged-in users
class NoteUpdateView(KuilaLoginRequiredMixin, UpdateView):
    model = Note  # Model to be used for the view
    fields = ['title', 'content', 'category']  # Fields to include in the form
    template_name = 'note/note_form_update.html'  # Template to render
    success_url = reverse_lazy('dashboard')  # Redirect URL after successful form submission

    def get_form(self, form_class=None):
        # Filter the category choices to only those belonging to the current user
        form = super().get_form(form_class)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        return form

    def get_object(self, queryset=None):
        # Get the note object by primary key and ensure it belongs to the current user
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk, user=self.request.user)

    def form_valid(self, form):
        # Set the user of the note to the current user
        form.instance.user = self.request.user
        return super().form_valid(form)


# View for deleting a note, restricted to logged-in users
class NoteDeleteView(KuilaLoginRequiredMixin, DeleteView):
    model = Note  # Model to be used for the view
    template_name = 'note/note_confirm_delete.html'  # Template to render
    success_url = reverse_lazy('dashboard')  # Redirect URL after successful deletion

    def get_object(self, queryset=None):
        # Get the note object by primary key and ensure it belongs to the current user
        pk = self.kwargs.get('pk')
        return get_object_or_404(Note, id=pk, user=self.request.user)