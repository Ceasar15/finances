from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import youth.views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('youth/',include("youth.urls")),
    path('youth/',include('pwa.urls')),
    path('', youth.views.index, name='home'),
    path('home/', youth.views.index),
    path('accounts/', include("accounts.urls")),
    path('newsletter/', include('newsletter.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)