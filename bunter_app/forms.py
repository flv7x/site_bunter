from django import forms
from .models import Cliente
from .models import Contact

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'cpf', 'email']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nome', 'email', 'titulo', 'mensagem']
