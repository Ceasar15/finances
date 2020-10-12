from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.template import RequestContext

from .models import Contact

# Create your views here.


def index(request):
    return render(request, "youth/index.html")

def about(request):
    return render(request, "youth/about.html")

def blog_single(request):
    return render(request, "youth/blog-single.html")

def blog(request):
    return render(request, "youth/blog.html")

def events(request):
    return render(request, "youth/events.html")

def sermons(request):
    return render(request, "youth/sermons.html")

def services(request):
    return render(request, "youth/services.html")

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('fullname') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('subject'):
            contact = Contact()
            contact.fullname = request.POST.get('fullname')
            contact.email = request.POST.get('email')
            contact.phone = request.POST.get('phone')
            contact.subject = request.POST.get('subject')
            contact.save()

            messages.success(request, "Thank you for reaching out to us.")
            
            #return HttpResponseRedirect('youth:index') 
            return render(request, "youth/contact.html")
            #return HttpResponseRedirect(reverse_lazy('index'))
    
    else:
        return render(request, "youth/contact.html")