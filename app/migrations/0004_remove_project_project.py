# Generated by Django 3.0.2 on 2020-01-18 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200118_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project',
        ),
    ]
