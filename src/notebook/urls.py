
from django.urls import path

from notebook.views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NotePreview

urlpatterns = [
    path('dashboard/', NoteListView.as_view(), name='dashboard'),
    path('create/', NoteCreateView.as_view(), name='note_create'),
    path('<str:pk>/preview/', NotePreview.as_view(), name='note_preview'),
    path('<str:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
