from __future__ import unicode_literals

from django.db import models

from image_cropping import ImageRatioField


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
    cropping = ImageRatioField('image', '430x360')
    album = models.ForeignKey('Album', related_name='album_photos')

    def __unicode__(self):
        return self.name

    def thumb(self):
        if self.image:
            return u'<img src="%s" width=60 height=60 />' % (self.image.url)
        else:
            return u'No image file found'
    thumb.short_description = ('Thumbnail')
