# coding: utf-8
from django.views.generic import (TemplateView, ListView, DetailView,
                                  FormView)
from django.core.urlresolvers import reverse_lazy

from .forms import ContactForm
from .models import (Home, AboutMe, Contact, HomePicture, ContactPicture)
from portifolio.models import Album


class HomesiteView(TemplateView):
    template_name = 'homesite/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomesiteView, self).get_context_data(**kwargs)
        context['home_information'] = Home.objects.first()
        if HomePicture.objects.count() > 1:
            context['photos'] = HomePicture.objects.all()
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

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['home_information'] = Home.objects.first()
        return context


class AlbumDetailMobileView(AlbumDetailView):
    template_name = 'homesite/album_detail_mobile.html'


class AboutMeView(TemplateView):
    template_name = 'homesite/about_me.html'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView, self).get_context_data(**kwargs)
        if AboutMe.objects.count() > 0:
            context['body'] = AboutMe.objects.first().body
            context['image'] = AboutMe.objects.first().picture.url
        return context


class ContactView(FormView):
    template_name = 'homesite/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['body'] = AboutMe.objects.first()
        context['company'] = Home.objects.first()
        if ContactPicture.objects.first():
            context['image'] = ContactPicture.objects.first().picture.url
        return context

    def form_valid(self, form):
        Contact.objects.create(**form.cleaned_data)
        return super(ContactView, self).form_valid(form)
