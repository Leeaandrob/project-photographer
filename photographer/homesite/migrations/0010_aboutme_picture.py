# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0009_homepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='picture',
            field=models.ImageField(default='', upload_to='homesite'),
            preserve_default=False,
        ),
    ]
