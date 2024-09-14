from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from users_profiles.models import KuilaUserProfile
from kuila.mixins import KuilaLoginRequiredMixin

# View to display user profile details
class UserProfile(KuilaLoginRequiredMixin, DetailView):
    model = KuilaUserProfile  # The model to use for this view (use the class instead of an instance)
    template_name = 'profile/index.html'  # Template to render
    context_object_name = 'user_profile'  # Name of the context variable to use in the template

    def get_object(self, queryset=None):
        # Get the profile for the currently logged-in user
        user = self.request.user.id
        user_profile = KuilaUserProfile.objects.get(user_id=user)  # Retrieve the profile based on user ID
        return user_profile

# View to update user profile details
class UserProfileUpdate(KuilaLoginRequiredMixin, UpdateView):
    model = KuilaUserProfile  # The model to use for this view
    fields = ['avatar', 'first_name', 'last_name', 'phone_number']  # Fields to include in the form
    template_name = 'profile/update.html'  # Template to render for the form
    success_url = reverse_lazy('profile')  # URL to redirect to upon successful form submission

    def get_object(self, queryset=None):
        # Get the profile for the currently logged-in user
        return KuilaUserProfile.objects.get(user=self.request.user)  # Retrieve the profile based on the logged-in user

    def form_valid(self, form):
        # Ensure that the profile being updated belongs to the current user
        if form.instance.user != self.request.user:
            return redirect('profile')  # Redirect if the profile does not belong to the current user
        return super().form_valid(form)  # Proceed with the form submission if the user is valid
