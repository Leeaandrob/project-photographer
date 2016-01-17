from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return self.name


class AboutMe(models.Model):
    body = models.TextField()


class HomePicture(models.Model):
    image_home = models.ImageField(upload_to='homesite/')


class Home(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_adress = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    pinterest = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.company_name
