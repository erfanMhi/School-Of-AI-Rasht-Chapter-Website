from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Lecture)
admin.site.register(Lecturer)
admin.site.register(Category)

