from django.contrib import admin
from django.http import HttpResponseForbidden
from .models import Task, Project
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)