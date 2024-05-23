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
    return render(request, 'produtos/produtos.html')
def sobre_mim(request):
    return render(request, 'sobre_mim/sobre_mim.html')
def compra(request):
    return render(request, 'compra/compra.html')
def mostruario(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/mostruario.html', {'produtos': produtos})

def CadastroCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Instancie o formulário correto
        if form.is_valid():
            form.save()
            return redirect('produto')  # Redireciona para a página de sucesso após o cadastro
    else:
        form = ClienteForm()  # Instancie o formulário correto
    return render(request, 'cadastro_cliente/cliente.html', {'form': form})