
from django.urls import path

from notebook.views import listview

urlpatterns = [
    path('list', listview, name='test')
]