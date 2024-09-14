from django.urls import path

# Importing the necessary views for category operations
from categories.views import CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryListView

# Defining URL patterns for the category-related views
urlpatterns = [
    # URL pattern for listing categories
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    # URL pattern for creating a new category
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    # URL pattern for updating a specific category (identified by its primary key)
    path('category/<str:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    # URL pattern for deleting a specific category (identified by its primary key)
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
