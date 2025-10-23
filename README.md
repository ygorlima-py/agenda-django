1 - Iniciar o projeto no Django

1.1 Criar Ambiente Virtual
python -m venv venv

1.2 Ativar ambiente virtual no Windows
venv\Scripts\activate

1.3 Instalar Django
pip intall django

1.4 Configurar requirements.txt
- Cria o arquivo requirements.txt
- pip freeze > requirements.txt 

1.5 Criar projeto
-django-admin startproject nome_do_projeto .

1.6 Configurar chave SSH windows
- Gere a chve usando o powershell
ssh-keygen -f $env:USERPROFILE\.ssh\qualquercoisa_rsa -t rsa -b 4096

- Gere a chave usando o gitbash
ssh-keygen -f ~/.ssh/qualquercoisa_rsa -t rsa -b 4096

- Autorize no gitbash (powershell não funciona)
$ eval $(ssh-agent) -> gera um Agent pid numero
$ ssh-add ~/.ssh/qualquercoisa_rsa 

2-Criando e modificando senha de superusuario em admin

python manage.py createsuperuser
python manage.py changepassword USERNAME