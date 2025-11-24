<template>
  <div class="home-container">
    <h1> Conheça o Sistema de Gestão de  Uso de Medicamentos! </h1>

    <p>
      Este sistema de controle de retiradas de medicamentos foi desenvolvido para otimizar o gerenciamento
      do uso de medicamentos por pacientes.<br><br>
      Com ele, é possível cadastrar medicamentos e pacientes, listar o que está cadastrado, e acompanhar o status do que está ativo de forma prática e segura.<br><br>
      Tecnologias modernas como <strong>Django</strong> (backend) e <strong>Vue.js</strong> (frontend)
      foram utilizadas na criação deste sistema, para proporcionar uma experiência amigável e um desempenho
      confiável, assegurando que as informações estejam sempre atualizadas e acessíveis.
    </p>

  </div>
</template>

<script>
  export default {
    name: "HomeView",
  };
</script>

<style scoped>
  .home-container {
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 25px;
    text-align: center;
  }

  h1 {
    color: #0f6a7a;
    font-size: 32px;
    margin-bottom: 30px;
  }

  p {
    color: #1b1b1b;
    font-size: 18px;
    line-height: 1.7;
    text-align: justify;
  }
</style>
