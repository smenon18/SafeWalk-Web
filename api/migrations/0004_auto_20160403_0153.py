# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160403_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='intransit',
            name='end_poss',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='intransit',
            name='est_distance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='intransit',
            name='start_pos',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
