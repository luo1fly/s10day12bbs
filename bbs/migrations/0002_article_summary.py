# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
