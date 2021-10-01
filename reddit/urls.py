from django.contrib import admin
from django.urls import path, include

""" django.conf package is imported to config media URL
    settings are imported because PROJECTNAME/settings.py file contain MEDIA_URL and MEDIA_ROOT configuration, and we need to add the configuration to PROJECT URL PATTERN.
"""
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
      path('admin/', admin.site.urls),
    path('', include('account.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
