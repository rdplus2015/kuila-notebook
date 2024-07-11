from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.generic import DeleteView, UpdateView

from users_accounts.form import SignUpForm, UserUpdateForm
from users_accounts.models import KuilaUser


class SignUp(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.get_success_url())
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')

    def get_redirect_url(self):
        return reverse('dashboard')


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={self.request.get_host()}):
            return next_url
        return reverse('dashboard')


@method_decorator(login_required, name='dispatch')
class UserLogout(LogoutView):
    next_page = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next')
        if next_url and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
            self.next_page = next_url
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """Prevents logout via GET request."""
        return HttpResponseNotAllowed(['POST'])


@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'profile/security/update_kuila_user_username.html'
    success_url = reverse_lazy('settings')


    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class DeleteUser(DeleteView):
    model = KuilaUser
    template_name = 'profile/security/delete_kuila_user.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Retourne l'objet KuilaUser associé à l'utilisateur connecté
        return self.model.objects.get(pk=self.request.user.pk)
