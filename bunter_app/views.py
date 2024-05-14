from django.shortcuts import redirect, render
from .forms import ClienteForm

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

def CadastroCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra')  # Redireciona para a página de sucesso após o salvamento
    else:
        form = ClienteForm()
    return render(request, 'cadastro_cliente/cadastro_clientes.html')