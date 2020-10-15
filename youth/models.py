from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(null=True, max_length=100, blank=True)
    email = models.EmailField(default="kwadwo123@gmail.com", max_length=100, blank=True)
    phone = models.IntegerField(null=True, blank=False)
    subject = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return str(self.fullname)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='blog_posts')
    updated_on = models.DateField(auto_now=True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    picture = models.ImageField(upload_to='blog_pics/', null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

