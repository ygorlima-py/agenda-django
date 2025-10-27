from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from contact.models import Contact
from django.urls import reverse

def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        context = dict(
            form=form,
            form_action=form_action,
        )

        print(context)

        if form.is_valid():
            print('Formulario Válido')
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk )

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


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        
        form = ContactForm(request.POST, instance=contact)
        
        context = dict(
            form=form,
            form_action=form_action,
        )

        if form.is_valid():
            print('Formulario Válido')
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk )

        return render(
        request,
        'contact/create.html',
        context,
        )

    context = dict(
        form=ContactForm(instance=contact)
    )

    return render(
        request,
        'contact/create.html',
        context, 
        )