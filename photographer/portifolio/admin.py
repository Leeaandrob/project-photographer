# coding: utf-8
from django.contrib import admin

from .models import (Category, Album, Photo)

admin.site.register(Category)
admin.site.register(Album)
admin.site.register(Photo)
