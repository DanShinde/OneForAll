# Generated by Django 4.1.7 on 2023-02-25 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('assigned_to', models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'projects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(choices=[('DEV', 'Development'), ('TEST', 'Testing'), ('DEPLOY', 'Deploying')], max_length=20)),
                ('assigned_to', models.ForeignKey(default='Admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dms.project')),
            ],
            options={
                'db_table': 'tasks',
                'managed': True,
            },
        ),
    ]
