from django.contrib import admin
from django.http import HttpResponseForbidden
from .models import SummitData
# Register your models here.

admin.site.register(SummitData)
