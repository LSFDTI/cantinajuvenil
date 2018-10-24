from django.contrib import admin
from .models import Campista 
from .models import Produto
from .models import Compra


admin.site.register(Campista)
admin.site.register(Produto)
admin.site.register(Compra)


#class CampistaAdmin(admin.ModelAdmin)
#	list_dysplay = ('nome', 'tribo')

# Register your models here.
