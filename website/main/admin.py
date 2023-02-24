from django.contrib import admin
from django.http import HttpResponseForbidden
from .models import Post
# Register your models here.

admin.site.register(Post)
