from django.http import request
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.views import generic

from .models import Post
from .models import Contact
from .forms import CommentForm

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


def blog_detail(request, slug):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "youth/blog-single.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("created_on")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm

    content = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'queryset': queryset,
    }

    return render(request, template_name, content)
