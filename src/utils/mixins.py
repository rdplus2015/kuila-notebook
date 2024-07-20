# utils/mixins.py

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class KuilaLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

    def handle_no_permission(self):
        from django.contrib import messages
        messages.add_message(self.request, messages.INFO, 'You need to be logged in to view this page.')
        return super().handle_no_permission()


"""
class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    permission_required = 'your_app.your_permission'
    login_url = '/login/'
    redirect_field_name = 'next'

    def handle_no_permission(self):
        from django.contrib import messages
        messages.add_message(self.request, messages.INFO, 'You do not have permission to view this page.')
        return super().handle_no_permission()

class CustomUserPassesTestMixin(UserPassesTestMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        from django.contrib import messages
        messages.add_message(self.request, messages.INFO, 'You do not have permission to view this page.')
        return super().handle_no_permission()

class SetUserInFormMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExtraContextMixin:
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class PaginationMixin:
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(self.get_queryset(), self.paginate_by)

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context['items'] = items
        return context

class CacheMixin:
    cache_timeout = 60 * 15  # 15 minutes

    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class FilterQuerySetMixin:
    filter_field = 'user'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_value = getattr(self.request, 'user', None)
        if filter_value:
            queryset = queryset.filter(**{self.filter_field: filter_value})
        return queryset
"""