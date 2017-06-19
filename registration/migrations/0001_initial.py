# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 05:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('intro', models.TextField(blank=True)),
                ('interests', models.TextField(blank=True)),
                ('expertise', models.TextField(blank=True)),
                ('gitHub', models.URLField(blank=True)),
                ('linkedIn', models.URLField(blank=True)),
                ('googlePlus', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('year', models.IntegerField(blank=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('typing_speed', models.IntegerField(blank=True, null=True)),
                ('is_mentor', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
