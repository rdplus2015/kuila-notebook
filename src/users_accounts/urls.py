from django.urls import path
from django.contrib.auth import views as auth_views

from users_accounts.views import SignUp, UserLogin, UserLogout, DeleteUser, UserUpdate

urlpatterns = [
    # User registration
    path('signup/', SignUp.as_view(), name='signup'),

    # User login
    path('login/', UserLogin.as_view(), name='login'),

    # User logout
    path('logout/', UserLogout.as_view(), name='logout'),

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    # Password change views
    path('settings/security/update/password/',
         auth_views.PasswordChangeView.as_view(template_name='profile/security/update_kuila_user_password.html'),
         name='update_kuila_user_password'),
    path('settings/security/update/password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='profile/security/password_change_done.html'),
         name='password_change_done'),

    # User profile update and account deletion
    path('settings/security/update/username/', UserUpdate.as_view(), name='update_kuila_user_username'),
    path('settings/security/deletemyaccount/', DeleteUser.as_view(), name='delete_kuila_user'),
]
