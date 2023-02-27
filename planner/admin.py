from django.contrib import admin
from django.http import HttpResponseForbidden
from .models import Task
# Register your models here.

admin.site.register(Task)
