from django.contrib import admin

from .models import Entidade,Contrato,TipoAmbiente,Ambiente, Alas

class ListaEntidades(admin.ModelAdmin):
    list_display = ('id', 'nome_razao')
    list_display_links = ('id', 'nome_razao')
    search_fields = ('nome_razao',)
    list_filter = ('tipo_entidade',)
    list_per_page = (10)

class ListaContrato(admin.ModelAdmin):
    list_display = ('id','busca_entidade','numero','ano','data_validade','prorrogavel')
    list_display_links = ('busca_entidade',)
    def busca_entidade(self,obj):
        return obj.entidade.nome_razao

    busca_entidade.short_description = 'Entidade'
    busca_entidade.admin_order_field = 'entidade__nome_razao'

class ListaAla(admin.ModelAdmin):
    list_display = ('id', 'nome', 'busca_entidade')
    list_display_links = ('nome',)

    def busca_entidade(self, obj):
        return obj.entidade.nome_razao

    busca_entidade.short_description = 'Entidade'
    busca_entidade.admin_order_field = 'entidade__nome_razao'


class ListaTipoAmbiente(admin.ModelAdmin):
    list_display = ('id','descricao','risco','controla_checklist')
    list_display_links = ('id','descricao')
    list_editable = ('controla_checklist',)
    filter_horizontal = ('checklists_relacionados',)

class ListaAmbiente(admin.ModelAdmin):
    list_display = ('id','busca_entidade','busca_tipo','descricao','codigo','area','andar','bloco')
    list_display_links = ('busca_entidade',)

    def busca_tipo(self,obj):
        return obj.tipo_ambiente.descricao

    busca_tipo.short_description = 'Tipo de Ambiente'
    busca_tipo.admin_order_field = 'tipoambiente__descricao'


    def busca_entidade(self,obj):
        return obj.entidade.nome_razao

    busca_entidade.short_description = 'Entidade'
    busca_entidade.admin_order_field = 'entidade__nome_razao'


admin.site.register(Entidade,ListaEntidades)
admin.site.register(Contrato,ListaContrato)
admin.site.register(TipoAmbiente,ListaTipoAmbiente)
admin.site.register(Ambiente,ListaAmbiente)
admin.site.register(Alas,ListaAla)