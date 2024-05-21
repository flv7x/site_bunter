from django.contrib import admin
from django.urls import path
from bunter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('produtos/', views.produto, name='produto'),
    path('sobre_mim/', views.sobre_mim, name='sobre_mim'),
    path('compra/', views.compra, name='compra'),
    path('lista_de_produto/', views.listar_produtos, name='lista_de_produto'),
    path('cadastro_cliente/', views.CadastroCliente, name='cadastro_clientes'),
]
