from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        lastst_name = cleaned_data.get('last_name')

        if first_name == lastst_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid',
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
                
            

        return super().clean()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
    )

    email = forms.EmailField()

    
    

    class Meta:
        model = User # Usamos o Objeto User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )


    # O método clen_email faz a validação usando atributo herdado da classe
    # UserCreationForm para pegar o valor do email e então validando usando
    # User.objects.filter(email=email).exists():
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email já cadastrado', code='invalid')
            )

        return email