from django.shortcuts import redirect, render
from .models import Cliente

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
        # Extrair os dados do formulário POST
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        
        # Criar uma instância do modelo Cliente com os dados do formulário
        novo_cliente = Cliente(nome=nome, sobrenome=sobrenome, cpf=cpf, email=email)
        
        # Salvar o novo cliente no banco de dados
        novo_cliente.save()
        
        # Redirecionar para uma página de sucesso após salvar os dados
        return redirect('pagina_sucesso')  # Altere 'pagina_sucesso' para a URL da sua página de sucesso

    # Se a solicitação não for do tipo POST, renderizar o formulário
    return render(request, 'cadastro_cliente/cadastro_clientes.html')  # Altere 'seu_template.html' para o nome do seu template de formulário