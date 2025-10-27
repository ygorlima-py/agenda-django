from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class': 'class-a',
            'placeholder': 'Digite seu nome'
            }
        ),
        label='Primeiro nome',
        help_text='Texto de ajuda para o meu usuário'
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'class-a',
        #     'placeholder': 'Digite seu nome'
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        )

        # Widgetes são tipos pra definir o tipo de campo que vai 
        # ser reenderizado, pode ser do tipo:
        # PasswordInput(), TextArea(), TextInput

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class-a',
        #             'placeholder': 'Digite seu nome'
        #         }
        #     ) 
        # }

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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid',
            )
        )
        return first_name