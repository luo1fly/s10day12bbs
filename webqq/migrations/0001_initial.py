# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 06:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bbs', '0006_userprofile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('mem_limits', models.IntegerField(default=200)),
                ('descriptions', models.TextField(max_length=256)),
                ('admins', models.ManyToManyField(related_name='admins', to='bbs.UserProfile')),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile')),
                ('members', models.ManyToManyField(auto_created=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile'), related_name='members', to='bbs.UserProfile')),
            ],
        ),
    ]