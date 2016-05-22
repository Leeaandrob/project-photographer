# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-22 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('client', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('1', 'One picture'), ('2', 'Two picture'), ('3', 'Full View')], default='1', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('index', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_photos', to='portifolio.Album')),
            ],
        ),
    ]
