from django.db import models
from events.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateTimeField(blank=True, null=True)
    province = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    photo_url = models.ImageField(blank=True, null=True, upload_to="users/images/%Y/%m/%D/")
    mobile = models.CharField(max_length=20, blank=True)
    events = models.ManyToManyField(Event, through='UserRegistration')

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class UserRegistration(models.Model):
    REG_STATUS = (
        ('r', 'Requested'),
        ('a', 'Accepted'),
        ('d', 'Declined'),
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    reg_status = models.CharField(max_length=1, choices=REG_STATUS)

    date_joined = models.DateTimeField(blank=True, null=True) # I should delete this

    def __str__(self):
        return self.reg_status
