from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters. '
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label='Password 2',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1') 
        password2 = self.cleaned_data.get('password2') 

        if password1 or password2:

            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas não correspondem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email') # Email digitado
        current_email = self.instance.email  # Email atual

        if current_email != email:
            if User.objects.filter(email=email).exists(): # Verifica se ja existe esse email cadastrado no banco
                self.add_error( # Adicionando erros aos campos
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1) # Validador de senha do Django

            except ValidationError as errors: # Se não passar adiciona erros aos campos
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )
        return password1