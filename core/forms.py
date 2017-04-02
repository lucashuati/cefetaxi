from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(label='Nome de Usuario', max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha', max_length=30)

CHOICES=[('motorista','Motorista'),
         ('associado','Associado')]

class NovoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput(), label='Senha', max_length=30)
    username = forms.CharField(label='Nome de Usuario', max_length=30)
    email = forms.EmailField(label='Email', max_length=30)
    tipo = forms.ChoiceField(label="Tipo", choices=CHOICES, widget=forms.RadioSelect())