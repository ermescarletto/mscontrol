from django.contrib import admin
from .models import *
# Register your models here.


class ListaTipoServico(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('descricao',)


#    def ambientes(self, obj):
#        text = ''
#        tipos = obj.tipo_ambiente.all()
#        for i in tipos:
#            text = text + i.descricao + "\n"
#        return text

class ListaCadastroChecklist(admin.ModelAdmin):

    filter_horizontal = ('itens',)



admin.site.register(TipoServico,ListaTipoServico)
admin.site.register(Servico)
admin.site.register(CadastroItemChecklist)
admin.site.register(CadastroChecklist,ListaCadastroChecklist)
admin.site.register(ChecklistPreenchido)
