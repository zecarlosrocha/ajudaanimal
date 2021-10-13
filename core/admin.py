from django.contrib import admin

from .models import Entidade

@admin.register(Entidade)
class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')