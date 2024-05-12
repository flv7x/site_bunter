from django.shortcuts import redirect, render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'homes/home.html')
def contato(request):
    return render(request, 'contato/contatos.html')
def produto(request):
    return render(request, 'produtos/produtos.html')
def sobre_mim(request):
    return render(request, 'sobre_mim/sobre_mim.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # type: ignore
        if form.is_valid():
            form.save()
            # Redirecione ou faça algo após o envio bem-sucedido do formulário
            return redirect('sucesso')
    else:
        form = ContactForm() # type: ignore
    return render(request, 'contato/contatos.html', {'form': form})