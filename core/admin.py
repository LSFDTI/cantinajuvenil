from django.contrib import admin
from .models import Campista 
from .models import Produto
from .models import Compra


class CampistaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'tribo','guardiao')

class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'valor', 'quantidade','total')

class CompraAdmin(admin.ModelAdmin):
	list_display = ('nome','produto','pago')

	
admin.site.register(Campista, CampistaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Compra, CompraAdmin)

