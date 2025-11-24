from django.contrib import admin
from .models import Categoria, Medicamento, Paciente, RegistroUso


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "apresentacao", "ativo")
    list_filter = ("categoria", "ativo")
    search_fields = ("nome",)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "documento", "telefone", "celular")
    search_fields = ("nome_completo", "documento")


@admin.register(RegistroUso)
class RegistroUsoAdmin(admin.ModelAdmin):
    list_display = ("paciente", "medicamento", "quantidade", "data_retirada", "ativo")
    list_filter = ("ativo", "data_retirada")
    search_fields = ("paciente__nome_completo", "medicamento__nome")