# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_coursebooking_courseregister_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='persons',
            field=models.IntegerField(default=0),
        ),
    ]
