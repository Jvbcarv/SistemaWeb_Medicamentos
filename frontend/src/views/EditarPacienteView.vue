<template>
  
  <div class="page">
    <h1> Editar Paciente </h1>

    <form @submit.prevent="atualizarPaciente">

      <!-- Nome Completo -->
      <div class="form-group">
        <label> Nome Completo: </label>
        <input type="text" v-model="form.nome_completo" required />
      </div>

      <!-- Data Nascimento -->
      <div class="form-group">
        <label> Data de Nascimento: </label>
        <input type="date" v-model="form.data_nascimento" required />
      </div>

      <!-- CPF -->
      <div class="form-group">
        <label> CPF: </label>
        <input
          type="text"
          v-model="form.cpf"
          @input="formatarCPF"
          maxlength="14"
          required
        />
      </div>

      <!-- Telefone -->
      <div class="form-group">
        <label> Telefone: </label>
        <input
          type="text"
          v-model="form.telefone"
          @input="formatarTelefone"
          maxlength="14"
        />
        <small class="info-opcional">Opcional</small>
      </div>

      <!-- Celular -->
      <div class="form-group">
        <label> Celular: </label>
        <input
          type="text"
          v-model="form.celular"
          @input="formatarCelular"
          maxlength="15"
        />
      </div>

      <button type="submit">Salvar Alterações</button>
      <button type="button" class="voltar" @click="$router.push('/pacientes')">
        Voltar
      </button>
    </form>

    <p v-if="mensagemSucesso" class="sucesso">{{ mensagemSucesso }}</p>
  </div>
</template>


<script>
    export default {
    name: "EditarPacienteView",

    data() {
        return {
        form: {
            nome_completo: "",
            data_nascimento: "",
            cpf: "",
            telefone: "",
            celular: "",
        },
        mensagemSucesso: "",
        idPaciente: null,
        };
    },

    mounted() {
        this.idPaciente = this.$route.params.id;
        this.carregarDados();
    },

    methods: {
        carregarDados() {
        fetch(`http://127.0.0.1:8000/api/pacientes/${this.idPaciente}/`)
            .then((res) => res.json())
            .then((data) => {
            this.form.nome_completo = data.nome_completo;
            this.form.data_nascimento = data.data_nascimento;
            this.form.cpf = data.documento; // voltar com máscara
            this.form.telefone = data.telefone;
            this.form.celular = data.celular;
            });
        },

        atualizarPaciente() {
        const atualizado = {
            nome_completo: this.form.nome_completo,
            data_nascimento: this.form.data_nascimento,
            documento: this.form.cpf.replace(/\D/g, ""),
            telefone: this.form.telefone.replace(/\D/g, ""),
            celular: this.form.celular.replace(/\D/g, ""),
        };

        fetch(`http://127.0.0.1:8000/api/pacientes/${this.idPaciente}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(atualizado),
        })
            .then((res) => {
            if (!res.ok) {
                alert("Erro ao atualizar!");
                return;
            }
            this.mensagemSucesso = "Atualizado com sucesso!";
            })
            .catch(() => alert("Erro inesperado ao atualizar."));
        },

        formatarCPF() {
        let cpf = this.form.cpf.replace(/\D/g, "");
        if (cpf.length > 3) cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
        if (cpf.length > 6) cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
        if (cpf.length > 9) cpf = cpf.replace(/(\d{3})(\d{2})$/, "$1-$2");
        this.form.cpf = cpf;
        },

        formatarTelefone() {
        let tel = this.form.telefone.replace(/\D/g, "");
        if (tel.length > 10) tel = tel.slice(0, 10);
        if (tel.length > 6) tel = tel.replace(/(\d{2})(\d{4})(\d+)/, "($1) $2-$3");
        else if (tel.length > 2) tel = tel.replace(/(\d{2})(\d+)/, "($1) $2");
        this.form.telefone = tel;
        },

        formatarCelular() {
        let tel = this.form.celular.replace(/\D/g, "");
        if (tel.length > 11) tel = tel.slice(0, 11);
        if (tel.length > 6) tel = tel.replace(/(\d{2})(\d{5})(\d+)/, "($1) $2-$3");
        else if (tel.length > 2) tel = tel.replace(/(\d{2})(\d+)/, "($1) $2");
        this.form.celular = tel;
        },
    },
   }; 
</script>


<style scoped>

    .page {
        padding: 0; 
        background: none;
        border-radius: 0;
        backdrop-filter: none;
        box-shadow: none;
        width: 50vw; /*largura */
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

    /* Layout do formulário */
    form {
        display: flex;
        flex-direction: column;
        gap: 18px;
    }

    /* Grupos dos campos */
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

    /* Inputs, Selects e Textareas */
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

    /* Efeito no campo input ao clicar */
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
        button.voltar {
        background-color: #17298b;
    }

    button.voltar:hover {
        background-color: #101e66;
    }

    .sucesso {   /* Mensagem de sucesso*/
        margin-top: 25px; /* distancia do texto do formulário */
        font-size: 20px; 
        font-weight: bold; /* negrito */
        text-align: center;
        color: #075e26;
        background-color: #c4f5d1; 
        border: 2px solid #0f6a7a;
        padding: 12px 16px;
        border-radius: 8px;
    }
</style>

