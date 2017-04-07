from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuario'}), label = '',max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),label = '', max_length=30)

CHOICES=[('motorista','Motorista'),
         ('associado','Associado')]

class NovoForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome'}),label = '', max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}),label = '', max_length=30)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome de Usuario'}),label = '', max_length=30)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}),label = '',max_length=30)
    tipo = forms.ChoiceField(label="", choices=CHOICES, widget=forms.RadioSelect())
