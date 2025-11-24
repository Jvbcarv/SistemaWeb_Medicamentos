<template> 
  <div class="page">
    <h1> Cadastrar Medicamento </h1>

    <form @submit.prevent="cadastrarMedicamento"> <!-- formulário não precisará recarregar a página ao enviar dados -->

      <!-- Campo Nome -->
      <div class="form-group">
        <label> Nome do medicamento: </label> 
        <input type="text" v-model="form.nome" required />
      </div>

      <!-- Campo Categoria -->
      <div class="form-group">
        <label>Categoria:</label>
        <select v-model="form.categoria" required>
          <option value=""> Selecione uma categoria: </option>
          <option v-for="cat in categorias" :key="cat.id" :value="cat.id"> <!-- Loop para listar categorias vindas do backend -->
            {{ cat.nome }}
          </option>
        </select>
      </div>

      <!-- Campo Apresentação -->
      <div class="form-group">
        <label> Apresentação: </label>
        <input type="text" v-model="form.apresentacao" placeholder="Exemplo: 325mg - 30 comprimidos."  required />
      </div>

      <!-- Botão Salvar -->
      <button type="submit">Salvar</button>
    </form>

    <!-- Mensagem "Medicamento cadastrado com sucesso!" - Ligação entre JavaScript e o HTML. -->
    <p v-if="mensagemSucesso" class="sucesso">{{ mensagemSucesso }}</p>
  </div>
</template>


<script>  
  export default {
    name: "CadastrarMedicamentoView",
    data() {
      return {
        // Objeto que guarda os valores preenchidos no formulário
        form: {
          nome: "",
          categoria: "",
          apresentacao: "",
          quantidade_estoque: "",
        },
        categorias: [], 
        mensagemSucesso: "",
      };
    },
    mounted() {
      fetch("http://127.0.0.1:8000/api/categorias/")
        .then(response => response.json())
        .then(data => {
          this.categorias = data;
        })
        .catch(err => console.error("Erro ao buscar categorias:", err));
    },

    methods: {     // Função executada quando o usuário clica em Salvar
      cadastrarMedicamento() {
        fetch("http://127.0.0.1:8000/api/medicamentos/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form), // Envia os dados para o backend
        })
          .then((response) => {
            if (!response.ok) throw new Error("Erro ao salvar!");
            return response.json();
          })
          .then(() => {
            this.mensagemSucesso = "Medicamento cadastrado com sucesso!";
            this.form = {
              nome: "",
              categoria: "",
              apresentacao: "",
              quantidade_estoque: "",
            };
          })
          .catch(() => alert("Erro ao cadastrar medicamento."));
      },
    },
  };
</script>


<style scoped>

  /* Caixa do formulário */
  .page {
    max-height: fit-content;
    margin: 100px auto;
    padding: 20px 25px;
    background: rgba(56, 115, 155, 0.15); 
    border-radius: 12px; 
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  }

  /* Título do formulario*/
  h1 { 
    text-align: center;
    margin-bottom: 8px;
    font-size: 28px;
    font-weight: bold;
    color: #0f6a7a; 
  }

  /* Espaçamento e alinhamento dos campos */
  form {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  /* Agrupamento */
  .form-group {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  /* Labels / rótulos do formulário */
  .form-group label {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
    color: #0f6a7a;
  }

  /* Inputs */
  .form-group input,
  .form-group select,
  .form-group textarea {
    padding: 8px;
    border-radius: 6px;
    border: 2px solid #c8d7df;
    outline: none;
    font-size: 14px;
  }

  .form-group input:focus,
  .form-group select:focus,
  .form-group textarea:focus {
    border-color: #0f6a7a; 
    box-shadow: 0 0 5px rgba(15,106,122,0.4);
  }

  /* Botão de Salvar */
  button {
    background-color: #0f6a7a;
    color: #ffffff;
    padding: 8px;
    border-radius: 10px;
    cursor: pointer;
    border: none;
    font-size: 16px;
    font-weight: bold;
    margin-top: 6px;
    transition: 0.3s;
  }
  button:hover {
    background-color: #0a4b56;
  }

  /* Mensagem de sucesso ao clicar no botão */
  .sucesso {
    margin-top: 25px; 
    font-size: 15px; 
    font-weight: bold; 
    text-align: center;
    color: #075e26;
    background-color: #c4f5d1; 
    border: 2px solid #0f6a7a;
    padding: 12px 16px;
    border-radius: 8px;
  }
</style>
