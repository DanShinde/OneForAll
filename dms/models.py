from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, default="Admin")
    class Meta:
        managed = True
        db_table = 'projects'

class Task(models.Model):
    DEVELOPMENT = 'DEV'
    TESTING = 'TEST'
    DEPLOYING = 'DEPLOY'
    TASK_TYPES = [
        (DEVELOPMENT, 'Development'),
        (TESTING, 'Testing'),
        (DEPLOYING, 'Deploying'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=20, choices=TASK_TYPES)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, default="Admin")
    class Meta:
        managed = True
        db_table = 'tasks'



"""from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ManyToManyField(User, related_name='project_assignments')
    # tasks = models.ManyToManyField(Task, related_name='projects')
    class Meta:
        managed = True
        db_table = 'projects'


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    employees = models.ManyToManyField(User, related_name='employees')
    is_validation_requested = models.BooleanField(default=False)
    is_validation_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'tasks'


"""