from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.generic import DeleteView, UpdateView

from users_accounts.form import SignUpForm, UserUpdateForm
from users_accounts.models import KuilaUser
from kuila.mixins import KuilaLoginRequiredMixin


# View for user sign-up
class SignUp(View):
    template_name = 'registration/signup.html'  # Template to render

    def get(self, request):
        # If the user is already authenticated, redirect to the dashboard
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm()  # Create an empty sign-up form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # If the user is already authenticated, redirect to the dashboard
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user
            return redirect(self.get_success_url())  # Redirect to success URL
        return render(request, self.template_name, {'form': form})  # Re-render the form with errors

    def get_success_url(self):
        # Get the URL to redirect to after successful sign-up
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')  # Default redirect to the dashboard

    def get_redirect_url(self):
        # Get the URL to redirect to if the user is already authenticated
        return reverse('dashboard')


# View for user login
class UserLogin(LoginView):
    template_name = 'registration/login.html'  # Template to render
    redirect_authenticated_user = True  # Redirect authenticated users to success URL

    def get_success_url(self):
        # Get the URL to redirect to after successful login
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')  # Default redirect to the dashboard


# View for user logout
class UserLogout(KuilaLoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')  # Default URL to redirect after logout

    def post(self, request, *args, **kwargs):
        # Handle logout via POST request and check if a custom next URL is provided
        next_url = request.POST.get('next')
        if next_url and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
            self.next_page = next_url
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Prevent logout via GET request."""
        return HttpResponseNotAllowed(['POST'])  # Only allow POST requests for logout


# View for updating user information
class UserUpdate(KuilaLoginRequiredMixin, UpdateView):
    model = get_user_model()  # Use the custom user model
    form_class = UserUpdateForm  # Form class for user updates
    template_name = 'profile/security/update_kuila_user_username.html'  # Template to render
    success_url = reverse_lazy('settings')  # Redirect URL after successful update

    def get_object(self, queryset=None):
        # Return the current user object
        return self.request.user


# View for deleting a user
class DeleteUser(KuilaLoginRequiredMixin, DeleteView):
    model = KuilaUser  # Model to be used for the view
    template_name = 'profile/security/delete_kuila_user.html'  # Template to render
    success_url = reverse_lazy('home')  # Redirect URL after successful deletion

    def get_object(self, queryset=None):
        # Return the user object associated with the current user
        return self.model.objects.get(pk=self.request.user.pk)
