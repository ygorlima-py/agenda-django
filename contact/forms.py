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
        
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='invalid',
            )
        )

        return super().clean()
