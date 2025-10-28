from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Rota para o usuário se cadastrar na plataforma
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Cadastrado com sucesso')
            return redirect('contact:login')



    return render(
        request,
        'contact/register.html',
        {
            'form':form,
        }
    )

# Rota para o usuário logar
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid(): # Retorna booleano verificando se os dados digitados são validos
            user = form.get_user() # Seleciona no banco o usuário 
            auth.login(request, user) # Faz a autentificação logando o usuário
            messages.success(request,'Você está logado') # Menssagem de sucesso do usuário logado
            return redirect('contact:index') # Redireciona para a pgina index home
        
        else:
            messages.error(request, 'Login Invalido')


    return render(
        request,
        'contact/login.html',
        {
            'form':form,
        }
    )


# Rota para deslogar o usuário
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


