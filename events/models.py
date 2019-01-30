from django.db import models

# Create your models here.

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    resume_url = models.FileField(max_length=200, upload_to="lecturers/resumes/%Y/%m/%D/", blank=True, null=True)
    photo_url = models.ImageField(max_length=200, upload_to="lecturers/resumes/%Y/%m/%D/", blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    organizer = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    cover_url = models.ImageField(max_length=100, upload_to="events/covers/%Y/%m/%D/")
    logo_url = models.ImageField(max_length=100, upload_to="events/logos/%Y/%m/%D/")

    categories = models.ManyToManyField(Category)

    description = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.title

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    lecturer = models.OneToOneField(
        Lecturer,
        on_delete=models.CASCADE,
        blank=True,
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.title










