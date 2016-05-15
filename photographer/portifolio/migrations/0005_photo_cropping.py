# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 15:37
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0004_album_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
