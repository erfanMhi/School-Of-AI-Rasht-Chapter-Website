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










