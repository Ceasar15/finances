from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .views import dashboard, profile, register

app_name = 'accounts'
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^profile/", profile, name="profile"),
    url(r"^", include("django.contrib.auth.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)