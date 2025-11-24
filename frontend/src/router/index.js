import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: "/medicamentos",
      name: "medicamentos",
      component: () => import("../views/MedicamentosView.vue"),
    },
    {
      path: "/cadastrar-medicamento",
      name: "cadastrar-medicamento",
      component: () => import("../views/CadastrarMedicamentoView.vue"),
    },
    {
      path: "/cadastrar-paciente",
      name: "cadastrar-paciente",
      component: () => import("../views/CadastrarPacienteView.vue"),
    },
    {
      path: "/pacientes",
      name: "pacientes",
      component: () => import("../views/PacientesView.vue"),
    },
    {
      path: "/registrar-uso",
      name: "registrar-uso",
      component: () => import("../views/RegistrarUsoView.vue"),
    },
    {
      path: "/registros-ativos",
      name: "registros-ativos",
      component: () => import("../views/RegistrosAtivosView.vue"),
    },
    {
      path: "/editar-paciente/:id",
      name: "EditarPaciente",
      component: () => import("../views/EditarPacienteView.vue"),
    },
    {
      path: "/editar-medicamento/:id",
      name: "EditarMedicamento",
      component: () => import("../views/EditarMedicamentoView.vue"),
    },
  ],
})

export default router
