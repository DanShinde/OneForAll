from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project, Task

@receiver(post_save, sender=Project)
def create_project_tasks(sender, instance, created, **kwargs):
    if created:
        # Define the list of tasks that should be generated for each project
        task_names = ['Document', 'Kick off meeting', 'Develop project', 'Test project']
        task_details = ['Onedrive Folder', 'Keep the date', 'Follow development Checklist', 'Test as per requirements']
        # Create a new task for each task name and add it to the project's task list
        for name,details in zip(task_names,task_details):
            task = Task.objects.create(name=name, description=details, is_validation_requested=False, is_validation_completed=False)
            instance.tasks.add(task)

        # Assign the project to the user who created it
        #instance.user.projects.add(instance)
