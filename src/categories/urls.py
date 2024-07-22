
from django.urls import path

from categories.views import CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryListView

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<str:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
