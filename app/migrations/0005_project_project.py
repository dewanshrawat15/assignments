# Generated by Django 3.0.2 on 2020-01-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_project_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project',
            field=models.FileField(default=0, upload_to='projects/'),
            preserve_default=False,
        ),
    ]
