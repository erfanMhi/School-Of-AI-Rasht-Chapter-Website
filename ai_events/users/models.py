from django.db import models
from events.models import *
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100, primary_key=True, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=100)

    events = models.ManyToManyField(Event, through='UserRegistration')

    def __str__(self):
        return self.user_name
    

class UserRegistration(models.Model):
    REG_STATUS = (
        ('r', 'Requested'),
        ('a', 'Accepted'),
        ('d', 'Declined'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    reg_status = models.CharField(max_length=1, choices=REG_STATUS)

    date_joined = models.DateTimeField()

    def __str__(self):
        return self.reg_status
