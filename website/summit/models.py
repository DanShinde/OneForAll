from django.db import models
from django.core.validators import MinLengthValidator

class SummitData(models.Model):
    task_name = models.CharField(max_length=255)
    task_notes = models.TextField(validators=[MinLengthValidator(50)])
    city = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    project_code = models.CharField(max_length=255)
    summit_username = models.IntegerField(unique=True)
    summit_password = models.CharField(max_length=255)
