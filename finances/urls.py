from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import youth.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', youth.views.index, name='home'),
    path('youth/', include("youth.urls")),
    path('accounts/', include("accounts.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)