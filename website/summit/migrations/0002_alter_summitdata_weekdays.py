# Generated by Django 4.1.7 on 2023-02-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summitdata',
            name='weekdays',
            field=models.CharField(max_length=255, null=True),
        ),
    ]