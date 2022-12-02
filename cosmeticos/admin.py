from django.contrib import admin
from cosmeticos.models import *
 
# Register your models here.
 
class PrincipalAdmim(admin.ModelAdmin):
    list_display = ('id', 'nome')
 
admin.site.register(Categoria)
admin.site.register(Produto, PrincipalAdmim)
 
