from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact

# Create your views here.
def index(request):
    page_obj = Contact.objects.filter(show=True).order_by('-id')
    
    paginator = Paginator(page_obj, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = dict(
        page_obj=page_obj,
        site_title='Contatos - '
    )
    return render(
        request,
        'contact/index.html',
        context,
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == ' ':
        return redirect('contact:index')

    page_obj = Contact.objects\
        .filter(show=True)\
        .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(phone__icontains=search_value) |
                Q(email__icontains=search_value) 
            )\
        .order_by('-id')

    paginator = Paginator(page_obj, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = dict(
        page_obj=page_obj,
        site_title='Search - '
    )
    return render(
        request,
        'contact/index.html',
        context,
    )

def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id, show=True).first()
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - ' # type: ignore
    if single_contact is None:
        raise Http404()
    
    context = {
        'contact': single_contact,
        'site_title': site_title
        }

    return render(
        request,
        'contact/contact.html',
        context,
    )

