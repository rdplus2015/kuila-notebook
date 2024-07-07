# Auth urls

from django.urls import path

from users_accounts.views import SignUp, UserLogin, UserLogout

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
