from django.contrib import admin

from tarefas.models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('nome',)