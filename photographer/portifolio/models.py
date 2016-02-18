from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    TYPE_ALBUM = (
        ('1', 'One picture'),
        ('2', 'Two picture'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    client = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=TYPE_ALBUM, default="1")

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    album = models.ForeignKey('Album', related_name='album_photos')

    def __unicode__(self):
        return self.name
