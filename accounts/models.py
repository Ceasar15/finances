from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields
    
    profile_pic = models.ImageField(upload_to= 'upload/')
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.profile_pic

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
    
# class Choices(models.Model):
#     choice = models.CharField(max_length=20, unique=True,)
class Finance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    date = models.DateField(auto_created=True, null= True)
    receipt = models.IntegerField(null=True, unique=True)
    types = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(null=True)
