# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signage', '0002_auto_20151230_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='use_frameset',
            field=models.BooleanField(default=False),
        ),
    ]
