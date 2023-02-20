from django.db import models

class Task(models.Model):
    TASK_STATUS = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )

    task_id = models.CharField(max_length=100, unique=True)
    task_name = models.CharField(max_length=100)
    bucket_name = models.CharField(max_length=100)
    progress = models.CharField(max_length=20, choices=TASK_STATUS)
    priority = models.CharField(max_length=20)
    created_by = models.CharField(max_length=100)
    created_date = models.DateField()
    assigned_to = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_recurring = models.BooleanField(default=False)
    late = models.BooleanField(default=False)
    completed_date = models.DateField(null=True, blank=True)
    completed_by = models.CharField(max_length=100, null=True, blank=True)
    completed_checklist_items = models.IntegerField(default=0)
    checklist_items = models.CharField(max_length=100, null=True, blank=True)
    labels = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.task_name
