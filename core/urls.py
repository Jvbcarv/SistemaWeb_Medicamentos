from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet,
    MedicamentoViewSet,
    PacienteViewSet,
    RegistroUsoViewSet,
    RegistrosAtivosList,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"medicamentos", MedicamentoViewSet)
router.register(r"pacientes", PacienteViewSet)
router.register(r"registros-uso", RegistroUsoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("registros-uso/lista/ativos/", RegistrosAtivosList.as_view(), name="registros-ativos"),
]