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
    
class Payments(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    fullname= models.CharField(max_length=100, null=True)
    email= models.EmailField(max_length=110, null=True)
    mobile_number= models.CharField(null=True, max_length=15)
    types= models.CharField(null=True, max_length=100)
    amount= models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.fullname)

@receiver(post_save, sender=Payments)
def create_payments(sender, instance, created, **kwargs):
    if created:
        Payments.objects.create(user=instance)

@receiver(post_save, sender=Payments)
def save_profile(sender, instance, **kwargs):
        instance.payments.save()

