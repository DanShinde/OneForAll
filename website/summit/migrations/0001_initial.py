# Generated by Django 4.1.7 on 2023-02-21 19:48

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
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('medium', models.CharField(max_length=255)),
                ('project_code', models.CharField(max_length=255)),
                ('summit_username', models.CharField(max_length=255)),
                ('summit_password', models.CharField(max_length=255)),
            ],
        ),
    ]