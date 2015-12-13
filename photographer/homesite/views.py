# coding: utf-8
from django.views.generic import (TemplateView, ListView, DetailView)

from portifolio.models import (Album, Category)


class HomesiteView(TemplateView):
    template_name = 'homesite/index.html'


class PortifolioListView(ListView):
    model = Album
    template_name = 'homesite/portifolio.html'
    context_object_name = 'albuns'

    def get_context_data(self, **kwargs):
        context = super(PortifolioListView, self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.all().order_by('name')
        return context


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'homesite/album_detail.html'
