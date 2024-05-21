from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import ClienteForm
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'homes/home.html')
def contato(request):
    return render(request, 'contato/contatos.html')
def produto(request):
    return render(request, 'produtos/produtos.html')
def sobre_mim(request):
    return render(request, 'sobre_mim/sobre_mim.html')
def compra(request):
    return render(request, 'compra/compra.html')
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_de_produtos.html', {'produtos': produtos})
    

def CadastroCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)  # Instancie o formulário correto
        if form.is_valid():
            form.save()
            return redirect('produto')  # Redireciona para a página de sucesso após o cadastro
    else:
        form = ClienteForm()  # Instancie o formulário correto
    return render(request, 'cadastro_cliente/cliente.html', {'form': form})