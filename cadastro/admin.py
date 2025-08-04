from django.contrib import admin
from .models import Estado, Cidade, Campus, GrupoTrabalho, Usuario, Edital


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome',)


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    list_filter = ('estado',)
    search_fields = ('nome',)


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    list_filter = ('cidade',)


@admin.register(GrupoTrabalho)
class GrupoTrabalhoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'matricula', 'campus')
    search_fields = ('nome', 'cpf', 'matricula')
    list_filter = ('campus', 'grupos')
    filter_horizontal = ('grupos',)


@admin.register(Edital)
class EditalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')
    search_fields = ('nome',)
