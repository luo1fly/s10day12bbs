# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webqq', '0002_auto_20160804_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qqgroup',
            name='members',
            field=models.ManyToManyField(related_name='members', to='bbs.UserProfile'),
        ),
    ]
