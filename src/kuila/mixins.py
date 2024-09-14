from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

# Custom mixin that extends Django's LoginRequiredMixin
class KuilaLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'  # URL to redirect to if the user is not logged in
    redirect_field_name = 'next'  # Name of the GET parameter to redirect to after login

    # Custom method to handle cases where the user does not have permission
    def handle_no_permission(self):
        from django.contrib import messages
        # Add a message to inform the user they need to be logged in
        messages.add_message(self.request, messages.INFO, 'You need to be logged in to view this page.')
        return super().handle_no_permission()

"""
The following mixins are commented out, but they provide additional functionality:

# Mixin for setting the current user in a form
class SetUserInFormMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user instance to the current user
        return super().form_valid(form)  # Proceed with the form submission

# Mixin for adding extra context to the view
class ExtraContextMixin:
    extra_context = {}  # Default to empty context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)  # Update context with extra_context
        return context  # Return the updated context

# Mixin for paginating querysets
class PaginationMixin:
    paginate_by = 10  # Number of items per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')  # Get current page from query parameters
        paginator = Paginator(self.get_queryset(), self.paginate_by)  # Initialize paginator

        try:
            items = paginator.page(page)  # Get items for the current page
        except PageNotAnInteger:
            items = paginator.page(1)  # If page is not an integer, show the first page
        except EmptyPage:
            items = paginator.page(paginator.num_pages)  # If page is out of range, show last page

        context['items'] = items  # Add items to context
        return context  # Return context with paginated items

# Mixin for caching views
class CacheMixin:
    cache_timeout = 60 * 15  # Cache timeout in seconds (15 minutes)

    @method_decorator(cache_page(cache_timeout))  # Apply cache_page decorator
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)  # Call parent dispatch method

# Mixin for filtering querysets based on a field
class FilterQuerySetMixin:
    filter_field = 'user'  # Default field to filter on

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the original queryset
        filter_value = getattr(self.request, 'user', None)  # Get filter value from request
        if filter_value:
            queryset = queryset.filter(**{self.filter_field: filter_value})  # Filter queryset
        return queryset  # Return the filtered queryset
"""
