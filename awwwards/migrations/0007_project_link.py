# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0006_auto_20181013_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.TextField(blank=True),
        ),
    ]