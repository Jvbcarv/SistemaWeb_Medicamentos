from rest_framework import serializers
from .models import Categoria, Medicamento, Paciente, RegistroUso


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria   #Tipo de remédio - exemplo: anti-inflamatório
        fields = "__all__"


class MedicamentoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source="categoria.nome", read_only=True)

    class Meta:
        model = Medicamento
        fields = [
            "id",
            "nome",
            "categoria",
            "categoria_nome",
            "apresentacao",
            "ativo",
        ]

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"


class RegistroUsoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    medicamento = MedicamentoSerializer(read_only=True)

    paciente_id = serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(), source="paciente", write_only=True
    )
    medicamento_id = serializers.PrimaryKeyRelatedField(
        queryset=Medicamento.objects.all(), source="medicamento", write_only=True
    )

    class Meta:
        model = RegistroUso
        fields = [
            "id",
            "paciente",
            "paciente_id",
            "medicamento",
            "medicamento_id",
            "quantidade",
            "data_retirada",
            "periodo_uso",
            "data_proxima_retirada",
            "data_final",
            "observacoes",
            "ativo",
        ]