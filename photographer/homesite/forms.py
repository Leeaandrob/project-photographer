# coding: utf-8
from __future__ import unicode_literals

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name',
                                           'class': 'inputForm2',
                                           'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'id': 'email',
                                            'class': 'inputForm2',
                                            'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'id': 'comments',
                                             'class': 'inputForm2'})}
