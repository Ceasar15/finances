from os import name
from django.urls import path
from django.conf.urls import url, include
from . import views


app_name = 'youth'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('sermons/', views.sermons, name='sermons'),
    path('services/', views.services, name='services'),
    url(r'^newsletter/', include('newsletter.urls')),
]