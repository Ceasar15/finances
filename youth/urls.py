from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'youth'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('sermons/', views.sermons, name='sermons'),
    path('services/', views.services, name='services'),
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog-single'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
