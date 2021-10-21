from django.contrib import admin

from .models import Entidade, Especie, Raca, Animal


@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'site', 'fone', 'modificado')


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'especie')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'entidade', 'imagem', 'ativo')