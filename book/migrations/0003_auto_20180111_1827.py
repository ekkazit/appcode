# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_register_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
