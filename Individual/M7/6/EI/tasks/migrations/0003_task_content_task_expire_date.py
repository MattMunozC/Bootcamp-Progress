# Generated by Django 5.0.4 on 2024-05-08 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.TextField(default='No description has been provided'),
        ),
        migrations.AddField(
            model_name='task',
            name='expire_date',
            field=models.DateField(default=datetime.date(2024, 5, 7)),
        ),
    ]
