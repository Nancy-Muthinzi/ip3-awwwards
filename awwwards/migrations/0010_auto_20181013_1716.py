# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0009_auto_20181013_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]
