# Generated by Django 5.0.4 on 2024-04-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
