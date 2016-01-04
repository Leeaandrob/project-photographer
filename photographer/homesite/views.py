# coding: utf-8
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, DetailView)

from .forms import ContactForm
from .models import (Home, AboutMe, Contact)
from portifolio.models import Album


class HomesiteView(TemplateView):
    template_name = 'homesite/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomesiteView, self).get_context_data(**kwargs)
        context['home_information'] = Home.objects.first()
        context['media'] = 'media/'
        context['photos'] = [photo.values()[0]
                             for photo in Album.objects.values(
                                 'album_photos__image')]
        return context


class PortifolioListView(ListView):
    model = Album
    template_name = 'homesite/portifolio.html'
    context_object_name = 'albuns'

    def get_context_data(self, **kwargs):
        context = super(PortifolioListView, self).get_context_data(**kwargs)
        context['home_information'] = Home.objects.first()
        return context


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'homesite/album_detail.html'


class AboutMeView(TemplateView):
    template_name = 'homesite/about_me.html'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        context['body'] = AboutMe.objects.first()
        return context


class ContactView(TemplateView):
    template_name = 'homesite/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['form'] = ContactForm(self.request.POST or None)
        context['body'] = AboutMe.objects.first()
        context['company'] = Home.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            Contact.objects.create(**context['form'].cleaned_data)
            messages.success(request, 'Cadastrado com sucesso')
