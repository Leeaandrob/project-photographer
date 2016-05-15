# coding: utf-8
from django.contrib import admin
from image_cropping import ImageCroppingMixin

from .models import (Album, Photo)


class PhotoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ["name", "thumb", "index", "album"]
    list_editable = ["index"]
    list_filter = ['album']

admin.site.register(Album)
admin.site.register(Photo, PhotoAdmin)
