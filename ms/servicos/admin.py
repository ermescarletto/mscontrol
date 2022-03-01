from django.contrib import admin
from .models import *
# Register your models here.




class ListaTipoServico(admin.ModelAdmin):
    list_display = ('id', 'descricao','ambientes')
    list_display_links = ('descricao',)
    filter_horizontal = ('tipo_ambiente',)
    list_filter = ('tipo_ambiente',)



    def ambientes(self, obj):
        text = ''
        tipos = obj.tipo_ambiente.all()
        for i in tipos:
            text = text + i.descricao + "\n"
        return text

admin.site.register(TipoServico,ListaTipoServico)
admin.site.register(Servico)
