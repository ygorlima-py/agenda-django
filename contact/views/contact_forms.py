from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = dict(
            form=form,
        )

        if form.is_valid():
            print('Formulario Válido')
            form.save()
            return redirect('contact:create')

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