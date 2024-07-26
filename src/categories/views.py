from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from categories.models import Category
from kuila.mixins import KuilaLoginRequiredMixin


class CategoryListView(KuilaLoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreateView(KuilaLoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category/category_form_create.html'
    fields = ['name']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(KuilaLoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category/category_form_update.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Category, id=pk, user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryDeleteView(KuilaLoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Category, id=pk, user=self.request.user)
