# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0002_auto_20151207_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]