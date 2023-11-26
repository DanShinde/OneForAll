from django.db import models

# Create your models here.
class Alarm(models.Model):
    triggerID = models.CharField(max_length=10)
    messageID = models.CharField(max_length=10)
    trigger = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

