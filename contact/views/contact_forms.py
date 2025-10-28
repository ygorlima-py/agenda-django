from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from contact.models import Contact
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        
        form = ContactForm(request.POST, request.FILES)
        
        context = dict(
            form=form,
            form_action=form_action,
        )

        print(context)

        if form.is_valid():        
            contact = form.save(commit=False) # Grarante que eu não salve na base de dados ainda
            contact.owner = request.user # Informo para contact.owner que esse contato pertence a esse usuário
            contact.save()
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

@login_required(login_url='contact:login')
def update(request, contact_id):

    print('usuário logado: ', request.user)

    # 1) Busca o contato pelo id; se não existir (ou show=False), ou se o usuário não for o dono do contato retorna 404
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)

    # 2) Monta a URL de action do form para essa própria view de update
    form_action = reverse('contact:update', args=(contact_id,))

    # 3) Se veio um POST, é tentativa de salvar alterações
    if request.method == 'POST':

        # 4) Cria o ModelForm já vinculado à instância existente (instance=contact)
        #    Isso faz o form executar UPDATE nesse contato (e não criar outro)
        form = ContactForm(request.POST, request.FILES, instance=contact)
        
        # 5) Contexto que será passado ao template (form + action do form)
        context = dict(
            form=form,
            form_action=form_action,
        )

        # 6) Valida os dados enviados
        if form.is_valid():
            print('Formulario Válido')

            # 7) Salva no banco (UPDATE na instância vinculada)
            contact = form.save()
            
            # 8) Redireciona para a própria página de update, já com o id do contato
            return redirect('contact:update', contact_id=contact.pk )

        # 9) Se form inválido, re-renderiza o template com erros
        return render(
        request,
        'contact/create.html',
        context,
        )
    

    # 10) Se for GET, monta o form pré-preenchido com os dados do contato
    context = dict(
        form=ContactForm(instance=contact)
    )

    # 11) Renderiza o template (o mesmo usado no create) com o form preenchido
    return render(
        request,
        'contact/create.html',
        context, 
        )


@login_required(login_url='contact:login')
def delete(request, contact_id):
    # 1) Busca o contato pelo id; se não existir (ou show=False), retorna 404
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)

    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation', confirmation)


    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )