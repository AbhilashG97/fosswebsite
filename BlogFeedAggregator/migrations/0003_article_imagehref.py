# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogFeedAggregator', '0002_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imageHref',
            field=models.URLField(null=True),
        ),
    ]
