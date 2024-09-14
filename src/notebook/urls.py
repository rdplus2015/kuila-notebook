from django.urls import path

from notebook.views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NotePreview

urlpatterns = [
    # URL pattern for listing notes
    path('note/list/', NoteListView.as_view(), name='note_list'),

    # URL pattern for creating a new note
    path('note/create/', NoteCreateView.as_view(), name='note_create'),

    # URL pattern for previewing a specific note
    path('note/<str:pk>/preview/', NotePreview.as_view(), name='note_preview'),

    # URL pattern for updating a specific note
    path('note/<str:pk>/update/', NoteUpdateView.as_view(), name='note_update'),

    # URL pattern for deleting a specific note
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note_delete'),
]
