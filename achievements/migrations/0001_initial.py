# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 17:02
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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('magazine', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('area', models.CharField(blank=True, max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.BigIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
                ('problems_solved', models.IntegerField()),
                ('ranking', models.BigIntegerField()),
                ('date', models.DateField()),
                ('description', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('contribution_id', models.CharField(max_length=200)),
                ('organisation', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gsoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=250)),
                ('mentors', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=400)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('internship', 'Internship'), ('masters', 'Masters'), ('exchange_student', 'Exchange programme')], max_length=100)),
                ('data', models.DateField()),
                ('area', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('talk', ' Talk'), ('demo', 'Demo'), ('workshop', 'Workshop'), ('paper', 'Paper Presentation'), ('other', 'Other')], max_length=100)),
                ('conference_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=300)),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
