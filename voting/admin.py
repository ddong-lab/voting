from django.contrib import admin

# Register your models here.
from .models import Candidate, Student


admin.site.register(Candidate)
admin.site.register(Student)
