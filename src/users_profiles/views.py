from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView

from users_profiles.models import KuilaUserProfile
from utils.mixins import KuilaLoginRequiredMixin


# Create your views here.

class UserProfile(KuilaLoginRequiredMixin, DetailView):
    model = KuilaUserProfile()
    template_name = 'profile/index.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        user = self.request.user.id
        user_profile = KuilaUserProfile.objects.get(user_id=user)
        return user_profile


class UserProfileUpdate(KuilaLoginRequiredMixin, UpdateView):
    model = KuilaUserProfile
    fields = ['first_name', 'last_name', 'phone_number']
    template_name = 'profile/update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return KuilaUserProfile.objects.get(user=self.request.user)

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            return redirect('profile')
        return super().form_valid(form)