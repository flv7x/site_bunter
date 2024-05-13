from django.contrib import admin
from .models import Contact
from .models import Cliente
from .models import Marca
from .models import Produto
from . models import Venda


admin.site.register(Contact)
admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Produto)
admin.site.register(Venda)