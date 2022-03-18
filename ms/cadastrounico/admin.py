from django.contrib import admin
from .models import *

class ListaPaises(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = (10)

class ListaEstados(admin.ModelAdmin):
    list_display = ('id','nome','uf')
    list_display_links = ('nome','uf')
    search_fields = ('nome',)
    list_filter = ('nome',)
    list_per_page = (10)

class ListaCidades(admin.ModelAdmin):
    list_display = ('id','nome','estado',)
    list_display_links = ('nome','estado',)
    search_fields = ('nome','estado',)
    list_filter = ('nome','estado',)
    list_per_page = (10)

class ListaLogradouros(admin.ModelAdmin):
    list_display = ('id','tipo_logradouro','nome')
    list_display_links = ('tipo_logradouro','nome')
    search_fields = ('tipo_logradouro','nome',)
    list_filter = ('tipo_logradouro','nome',)
    list_per_page = (10)

class ListaPessoas(admin.ModelAdmin):
    list_display = ('id','tipo_pessoa','nome','cpfcnpj')
    list_display_links = ('nome',)
    search_fields = ('tipo_pessoa','nome','cpfcnpj')
    list_filter = ('tipo_pessoa',)
    list_per_page = (10)






admin.site.register(Cidade,ListaCidades)
admin.site.register(Logradouro,ListaLogradouros)
admin.site.register(Pais,ListaPaises)
admin.site.register(Estado,ListaEstados)
admin.site.register(Pessoa,ListaPessoas)
