# Generated by Django 3.0.2 on 2020-01-18 06:41

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200118_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.FileField(upload_to=app.models.get_upload_path),
        ),
    ]
