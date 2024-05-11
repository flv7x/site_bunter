from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homes/home.html')

def contato(request):
    return render(request, 'contato/contatos.html')