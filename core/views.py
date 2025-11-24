from rest_framework import viewsets, generics
from .models import Categoria, Medicamento, Paciente, RegistroUso
from .serializers import (
    CategoriaSerializer,
    MedicamentoSerializer,
    PacienteSerializer,
    RegistroUsoSerializer,
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


from rest_framework import viewsets, generics
from django.utils import timezone
from django.db.models import Q
from .models import Categoria, Medicamento, Paciente, RegistroUso
from .serializers import (
    CategoriaSerializer,
    MedicamentoSerializer,
    PacienteSerializer,
    RegistroUsoSerializer,
)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class RegistroUsoViewSet(viewsets.ModelViewSet):
    queryset = RegistroUso.objects.all()
    serializer_class = RegistroUsoSerializer

class RegistrosAtivosList(generics.ListAPIView):
    serializer_class = RegistroUsoSerializer

    def get_queryset(self):
        hoje = timezone.now().date()
        return RegistroUso.objects.filter(
            Q(data_final__isnull=True) | Q(data_final__gte=hoje),
            ativo=True
        )