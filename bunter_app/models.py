from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Cliente(models.Model):  # Renomeado para seguir a convenção de nomenclatura
    nome = models.CharField(max_length=30, blank=False, null=False)
    sobrenome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True)  # Adicionado unique=True
    email = models.EmailField(blank=False, null=False)
    
    def __str__(self):
        return self.nome

class Marca(models.Model):  # Renomeado para seguir a convenção de nomenclatura
    nome = models.CharField(max_length=30, blank=False, null=False)  # Renomeado para nome

    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=70)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=8, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.descricao
    
class Venda(models.Model):  # Renomeado para seguir a convenção de nomenclatura
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto)  # Alterado para ManyToManyField para permitir vários produtos por venda
    total_compra = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    
    def __str__(self):
        return self.cliente


