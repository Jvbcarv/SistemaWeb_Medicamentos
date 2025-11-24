<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <h1>Sistema de Gestão de Uso de Medicamentos</h1>
      <nav>
        <router-link to="/"> Sobre o Sistema </router-link><br>
        <router-link to="/cadastrar-medicamento"> Cadastro de Medicamentos </router-link>
        <router-link to="/medicamentos"> Listagem de Medicamentos por Categoria </router-link><br>
        <router-link to="/cadastrar-paciente"> Cadastro de Paciente </router-link>
        <router-link to="/pacientes"> Listagem de Pacientes Cadastrados </router-link><br>
        <router-link to="/registrar-uso"> Registrar Retirada de Medicamento </router-link>
        <router-link to="/registros-ativos"> Listagem de Registros Ativos </router-link>
      </nav>
    </div>
  </header>

  <router-view />
</template>


<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

h1 {
  color: #0f6a7a;
  font-size: 40px;
  font-weight: bold;
  margin-bottom: 40px; 
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  color: #ffffff
}

nav a.router-link-exact-active {
  color: #0f6a7aff;
}

nav a.router-link-exact-active:hover {
  background-color: #ffffffff; /*cor ao passar o mouse sobre o nav selecionado*/
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}
nav {
  background-color: rgba(56, 115, 155, 0.15); 
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  padding: 10px;
  border-radius: 8px;
}
nav { /* fica em coluna */
  display: flex;
  flex-direction: column; 
  gap: 5px; /* espaço entre os links */
  align-items: left;
}
nav a {
  font-size: 15px;
  font-weight: 500;
  color: #0f6a7a; /* azul do seu layout */
  text-decoration: none; /* remove underline */
  padding: 8px 10px;
  border-radius: 6px;
  transition: 0.3s;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}

</style>
