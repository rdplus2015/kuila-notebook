
from django.urls import path

from users_profiles.views import UserProfile, UserProfileUpdate

urlpatterns = [
    path('profile/', UserProfile.as_view(), name='profile'),
    path('profile/update/', UserProfileUpdate.as_view(), name='profile_update'),
]
