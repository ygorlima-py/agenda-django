from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact


def create(request):

    context = dict(
    )

    return render(
        request,
        'contact/create.html',
        context,
    )