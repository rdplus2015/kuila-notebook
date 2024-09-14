"""
URL configuration for the kuila project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL configuration:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# Importing views for the home page, dashboard, and settings
from kuila.views import Home, SettingsView, Dashboard

from django.conf import settings
from django.conf.urls.static import static

# Defining the URL patterns for the application
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # URL for the dashboard page
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    # URL for the settings page
    path('settings/', SettingsView.as_view(), name='settings'),

    # URL for the home page
    path('', Home.as_view(), name='home'),

    # Including URLs from the 'users_accounts', 'users_profiles', 'notebook', and 'categories' apps
    path('', include('users_accounts.urls')),
    path('', include('users_profiles.urls')),
    path('', include('notebook.urls')),
    path('', include('categories.urls')),

    # URL for the CKEditor file uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Serving media files in development mode when DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
