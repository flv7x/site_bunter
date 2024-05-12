from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homes/home.html')
def contato(request):
    return render(request, 'contato/contatos.html')
def produto(request):
    return render(request, 'produtos/produtos.html')
def sobre_mim(request):
    return render(request, 'sobre_mim/sobre_mim.html')