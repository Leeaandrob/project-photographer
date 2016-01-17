from django.contrib import admin

from .models import (Home, AboutMe, Contact, HomePicture, ContactPicture)

admin.site.register(Home)
admin.site.register(AboutMe)
admin.site.register(Contact)
admin.site.register(HomePicture)
admin.site.register(ContactPicture)
