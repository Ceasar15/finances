from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(null=True, max_length=100, blank=True)
    email = models.EmailField(default="kwadwo123@gmail.com", max_length=100, blank=True)
    phone = models.IntegerField(null=True, blank=False)
    subject = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return str(self.fullname)

