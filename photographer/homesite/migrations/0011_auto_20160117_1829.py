# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0010_aboutme_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='contact/')),
            ],
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='picture',
            field=models.ImageField(upload_to='about_me'),
        ),
    ]
