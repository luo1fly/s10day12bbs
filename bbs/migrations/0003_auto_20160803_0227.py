# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(auto_created='statics/imgs/upload/', upload_to=''),
        ),
    ]