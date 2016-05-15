from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe

from image_cropping import ImageRatioField


class Album(models.Model):
    TYPE_ALBUM = (
        ('1', 'One picture'),
        ('2', 'Two picture'),
        ('3', 'Full View'),
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
    cropping = ImageRatioField('image', '430x360')
    album = models.ForeignKey('Album', related_name='album_photos')
    index = models.IntegerField()

    def __unicode__(self):
        return self.name

    def thumb(self):
        if self.image:
            path = u'<img src="http://edixonphotography.com%s" width=320 height=180 />' % (self.image.url)
            return mark_safe(path)
        else:
            return u'No image file found'
    thumb.short_description = ('Thumbnail')
