# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 13:10
from __future__ import unicode_literals

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20180112_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='outline',
            field=models.FileField(blank=True, null=True, upload_to=course.models.get_course_outline_file),
        ),
    ]
