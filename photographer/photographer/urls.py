# coding: utf-8
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from homesite.views import (HomesiteView, PortifolioListView,
                            AlbumDetailView, AboutMeView, ContactView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomesiteView.as_view(), name='home'),
    url(r'^about_me/', AboutMeView.as_view(), name='about_me'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^portifolio/$', PortifolioListView.as_view(), name='portifolio'),
    url(r'^portifolio/(?P<pk>\d+)/$', AlbumDetailView.as_view(),
        name='album')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
