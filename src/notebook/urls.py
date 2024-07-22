
from django.urls import path

from notebook.views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NotePreview

urlpatterns = [
    path('note/list/', NoteListView.as_view(), name='note_list'),
    path('note/create/', NoteCreateView.as_view(), name='note_create'),
    path('note/<str:pk>/preview/', NotePreview.as_view(), name='note_preview'),
    path('note/<str:pk>/update/', NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
