from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid',
            )
        )

        return super().clean()

def create(request):
    if request.method == 'POST':
        context = dict(
            form=ContactForm(request.POST),
        )

        return render(
        request,
        'contact/create.html',
        context,
        )

    context = dict(
        form=ContactForm()
    )

    return render(
        request,
        'contact/create.html',
        context, 
        )