from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    client = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    album = models.ForeignKey('Album', related_name='album_photos')

    def __unicode__(self):
        return self.name
