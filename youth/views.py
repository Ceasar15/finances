from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from .models import Post
from .models import Contact

# Create your views here.


def index(request):
    return render(request, "youth/index.html")

def about(request):
    return render(request, "youth/about.html")

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
             
            return render(request, "youth/contact.html")

    
    else:
        return render(request, "youth/contact.html")

class BlogList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "youth/blog.html"
    paginate_by = 3

class BlogDetail(generic.DetailView):
    model = Post
    template_name = "youth/blog-single.html"

