from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
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