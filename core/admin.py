from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms.forms import EntidadeCreateForm, EntidadeChangeForm
from .models import Entidade, Especie, Raca, Animal


@admin.register(Entidade)
class EntidadeAdmin(UserAdmin):
    add_form = EntidadeCreateForm
    form = EntidadeChangeForm
    model = Entidade
    list_display = ('email', 'nome', 'fone', 'cidade', 'uf', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'fone', 'cidade', 'uf')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')


@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'especie')


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'entidade', 'imagem', 'imagem_small', 'ativo', 'entidade')
    search_fields = ['nome', 'raca', 'entidade', 'ativo', 'entidade__nome']

    def save_model(self, request, obj, form, change):
        obj = form.save(commit=False)
        obj.entidade = request.user
        obj.save
