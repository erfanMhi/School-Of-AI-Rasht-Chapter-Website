from django.db import models

# Create your models here.

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    resume_url = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    lecturer = models.OneToOneField(
        Lecturer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    organizer = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    cover_url = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=100)

    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

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









