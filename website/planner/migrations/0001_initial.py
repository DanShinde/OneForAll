# Generated by Django 4.1.7 on 2023-02-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=100, unique=True)),
                ('task_name', models.CharField(max_length=100)),
                ('bucket_name', models.CharField(max_length=100)),
                ('progress', models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
                ('priority', models.CharField(max_length=20)),
                ('created_by', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('assigned_to', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('is_recurring', models.BooleanField(default=False)),
                ('late', models.BooleanField(default=False)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('completed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('completed_checklist_items', models.IntegerField(default=0)),
                ('checklist_items', models.CharField(blank=True, max_length=100, null=True)),
                ('labels', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
