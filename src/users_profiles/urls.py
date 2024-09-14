from django.urls import path

from users_profiles.views import UserProfile, UserProfileUpdate

urlpatterns = [
    # URL pattern for viewing the user profile
    path('profile/', UserProfile.as_view(), name='profile'),

    # URL pattern for updating the user profile
    path('profile/update/', UserProfileUpdate.as_view(), name='profile_update'),
]
