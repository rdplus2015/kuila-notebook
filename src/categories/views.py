from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Import necessary generic views for creating, listing, updating, and deleting objects
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Importing the Category model and a custom login-required mixin
from categories.models import Category
from kuila.mixins import KuilaLoginRequiredMixin


# View for listing all categories that belong to the current user
class CategoryListView(KuilaLoginRequiredMixin, ListView):
    model = Category  # Specifies the model to use for the view
    template_name = 'category/index.html'  # Defines the template for rendering the view
    context_object_name = 'categories'  # Specifies the name of the context variable in the template

    # Overriding the get_queryset method to return only categories for the logged-in user
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)  # Filters categories by the current user


# View for creating a new category
class CategoryCreateView(KuilaLoginRequiredMixin, CreateView):
    model = Category  # Specifies the model to use
    template_name = 'category/category_form_create.html'  # Template for rendering the create form
    fields = ['name']  # Fields to include in the form
    success_url = reverse_lazy('dashboard')  # URL to redirect to upon successful form submission

    # Overriding form_valid to assign the category to the current user before saving
    def form_valid(self, form):
        form.instance.user = self.request.user  # Automatically assign the logged-in user to the category
        return super().form_valid(form)  # Call the parent method to handle the rest


# View for updating an existing category
class CategoryUpdateView(KuilaLoginRequiredMixin, UpdateView):
    model = Category  # Specifies the model to use
    fields = ['name']  # Fields to include in the form
    template_name = 'category/category_form_update.html'  # Template for the update form
    success_url = reverse_lazy('dashboard')  # URL to redirect to after a successful update

    # Overriding get_object to ensure the user can only update their own categories
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')  # Get the primary key from the URL
        return get_object_or_404(Category, id=pk, user=self.request.user)  # Fetch the category that belongs to the user

    # Overriding form_valid to ensure the category remains associated with the user during an update
    def form_valid(self, form):
        form.instance.user = self.request.user  # Ensure the category remains associated with the current user
        return super().form_valid(form)  # Call the parent method to handle the form submission


# View for deleting an existing category
class CategoryDeleteView(KuilaLoginRequiredMixin, DeleteView):
    model = Category  # Specifies the model to use
    template_name = 'category/category_confirm_delete.html'  # Template for confirming the deletion
    success_url = reverse_lazy('dashboard')  # URL to redirect to after successful deletion

    # Overriding get_object to ensure the user can only delete their own categories
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')  # Get the primary key from the URL
        return get_object_or_404(Category, id=pk, user=self.request.user)  # Ensure the user can delete only their own category
