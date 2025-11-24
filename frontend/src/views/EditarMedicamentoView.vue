<template>
  
  <div class="page">
    <h1>Editar Medicamento</h1>

    <form @submit.prevent="atualizarMedicamento">

      <div class="form-group">
        <label>Nome:</label>
        <input type="text" v-model="form.nome" required />
      </div>

      <div class="form-group">
        <label>Categoria:</label>
        <select v-model="form.categoria" required>
          <option value="">Selecione a categoria</option>
          <option v-for="cat in categorias" :key="cat.id" :value="cat.id">
            {{ cat.nome }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>Apresentação:</label>
        <textarea v-model="form.apresentacao" rows="2" required></textarea>
      </div>

      <div class="form-group">
        <label>Status:</label>
        <select v-model="form.ativo">
          <option :value="true">Ativo</option>
          <option :value="false">Inativo</option>
        </select>
      </div>

      <button type="submit">Salvar Alterações</button>
      <button type="button" class="voltar" @click="$router.push('/medicamentos')">
        Voltar
      </button>
    </form>

    <p v-if="mensagemSucesso" class="sucesso">{{ mensagemSucesso }}</p>
  </div>
</template>


<script>
    export default {
    name: "EditarMedicamentoView",

    data() {
        return {
        form: {},
        categorias: [],
        mensagemSucesso: "",
        idMedicamento: null,
        };
    },

    mounted() {
        this.idMedicamento = this.$route.params.id;
        this.carregarCategorias();
        this.carregarMedicamento();
    },

    methods: {
        carregarCategorias() {
        fetch("http://127.0.0.1:8000/api/categorias/")
            .then(res => res.json())
            .then(data => {
            this.categorias = data;
            });
        },

        carregarMedicamento() {
        fetch(`http://127.0.0.1:8000/api/medicamentos/${this.idMedicamento}/`)
            .then(res => res.json())
            .then(data => {
            this.form = data;
            })
            .catch(() => alert("Erro ao carregar medicamento"));
        },

        atualizarMedicamento() {
        fetch(`http://127.0.0.1:8000/api/medicamentos/${this.idMedicamento}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.form),
        })
            .then(res => {
            if (!res.ok) {
                alert("Erro ao atualizar medicamento");
                return;
            }
            this.mensagemSucesso = "Atualizado com sucesso!";
            })
            .catch(() => alert("Erro inesperado ao atualizar"));
        },
    },
    };
</script>


<style scoped>

    /* Caixa do formulário */
    .page {
        padding: 0;
        background: none;
        border-radius: 0;
        backdrop-filter: none;
        box-shadow: none;
        width: 50vw;
        max-width: 500px;
        margin: 0 auto;
    }

    /* Título */
    h1 {
        text-align: center;
        margin-bottom: 20px;
        font-size: 28px;
        font-weight: bold;
        color: #0f6a7a;
    }

    /* Layout dos campos */
    form {
        display: flex;
        flex-direction: column;
        gap: 18px;
    }

    /* Agrupamento */
    .form-group {
        display: flex;
        flex-direction: column;
    }

    /* Labels */
    .form-group label {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 5px;
        color: #0f6a7a;
    }

    /* inputs selects e textareas */
    .form-group input,
    .form-group select,
    .form-group textarea {
        padding: 12px;
        border-radius: 6px;
        border: 2px solid #c8d7df;
        font-size: 15.5px;
        color: #0d272c;
        outline: none;
        font-family: inherit;
        background-color: #ffffffcc;
        resize: vertical;
    }

    /* efeito em clicar na input */
    .form-group input:focus,
    .form-group select:focus,
    .form-group textarea:focus {
        border-color: #0f6a7a;
        box-shadow: 0 0 6px rgba(15, 106, 122, 0.4);
    }

    /* Botões */
    button {
        padding: 12px;
        border-radius: 10px;
        cursor: pointer;
        border: none;
        font-size: 16px;
        font-weight: bold;
        background-color: #0f6a7a;
        color: #fff;
        transition: 0.3s;
    }
    button:hover {
        background-color: #0a4b56;
    }

    /* Botão Voltar */
    .voltar {
        background-color: #17298b;
    }
    .voltar:hover {
        background-color: #101e66;
    }

    /* Mensagem de sucesso */
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
