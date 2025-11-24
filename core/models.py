from django.db import models
from django.utils import timezone

#Categoria de medicamentos
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    descricao = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome

# Nome do medicamento, apresentação dele, quantidade em estoque, se está ativo ou não
class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="medicamentos"
    )
    apresentacao = models.TextField() 
    quantidade_estoque = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.apresentacao}"

# Dados do paciente
class Paciente(models.Model):
    nome_completo = models.CharField(max_length=150)
    documento = models.CharField(max_length=50, blank=True)  #CPF
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_completo

# Registro de uso do medicamento
class RegistroUso(models.Model):
    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.PROTECT,
        related_name="registros_de_uso"
    )
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name="registros_do_paciente"
    )
    quantidade = models.CharField(max_length=50)
    data_retirada = models.DateField(null=True, blank=True)
    
    periodo_uso = models.CharField(max_length=100, blank=True)
    
    data_proxima_retirada = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)

    observacoes = models.TextField(blank=True)

    # Controle da listagem ativa
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.paciente} - {self.medicamento} ({self.quantidade})"
