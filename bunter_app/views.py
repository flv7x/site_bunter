from django.shortcuts import redirect, render
from django.http import JsonResponse
from .forms import ContatoForm
from .forms import ClienteForm
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'homes/home.html')
def contato(request):
    if request.method == 'POST':
        formContact = ContatoForm(request.POST)
        if formContact.is_valid():
            formContact.save()
            return redirect('home')  
    else:
        formContact = ContatoForm()
    return render(request, 'contato/contatos.html', {'form': formContact})
        
def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})
def sobre_mim(request):
    return render(request, 'sobre_mim/sobre_mim.html')
def compra(request):
    return render(request, 'compra/compra.html')

def CadastroCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('produto')
    else:
        form = ClienteForm()
    return render(request, 'cadastro_cliente/cliente.html', {'form': form})