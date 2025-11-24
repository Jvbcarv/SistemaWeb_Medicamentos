<template>

  <div class="page">

    <h1> Cadastrar Paciente </h1>
    <form @submit.prevent="cadastrarPaciente">

      <!-- campo Nome -->
      <div class="form-group">
        <label> Nome Completo: </label>
        <input type="text" v-model="form.nome_completo" required />
      </div>

      <!-- Data de Nascimento com input tipo data -->
      <div class="form-group">
        <label> Data de Nascimento: </label>
        <input type="date" v-model="form.data_nascimento" required />
      </div>

      <!-- campo CPF com máscara -->
      <div class="form-group">
        <label> CPF: </label>
        <input
          type="text"
          v-model="form.cpf"
          @input="formatarCPF"
          maxlength="14"
          placeholder="000.000.000-00"
          required
        />
      </div>
      
      <!-- Telefone com máscara-->
      <div class="form-group">
        <label> Telefone: </label>
        <input
          type="text"
          v-model="form.telefone"
          @input="formatarTelefone"
          maxlength="14"
          placeholder="(00) 0000-0000"
        />
        <small class="info-opcional"> Opcional </small>
      </div>

      <!-- Celular com máscara-->
      <div class="form-group">
        <label> Celular: </label>
        <input
          type="text"
          v-model="form.celular"
          @input="formatarCelular"
          maxlength="15"
          placeholder="(00) 00000-0000"
        />
      </div>

      <!-- botão-->
      <button type="submit">Salvar</button>
    </form>

    <!-- Mensagem de sucesso-->
    <p v-if="mensagemSucesso" class="sucesso">{{ mensagemSucesso }}</p>
  </div>

</template>


<script> 
  export default {
    name: "CadastrarPacienteView",
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
      };
    },
    methods: {
      formatarCPF() {
        let cpf = this.form.cpf.replace(/\D/g, ""); // para remover tudo que não é número

        if (cpf.length > 3) cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
        if (cpf.length > 6) cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");
        if (cpf.length > 9) cpf = cpf.replace(/(\d{3})(\d{2})$/, "$1-$2");

        this.form.cpf = cpf;
      },

      formatarTelefone() {
          let tel = this.form.telefone.replace(/\D/g, ""); 

           if (tel.length > 10) tel = tel.slice(0, 10); // telefone fixo tem 10 dígitos

            if (tel.length > 6) {
              // quando tiver DDD + 4 primeiros + resto
              tel = tel.replace(/(\d{2})(\d{4})(\d+)/, "($1) $2-$3");
            } else if (tel.length > 2) {
              tel = tel.replace(/(\d{2})(\d+)/, "($1) $2");
            } else {
              tel = tel.replace(/(\d+)/, "($1");
            }

          this.form.telefone = tel;
        },

      formatarCelular() {
          let tel = this.form.celular.replace(/\D/g, "");
          
          if (tel.length > 11) tel = tel.slice(0, 11);

          if (tel.length > 6) {
            tel = tel.replace(/(\d{2})(\d{5})(\d+)/, "($1) $2-$3");
          } else if (tel.length > 2) {
            tel = tel.replace(/(\d{2})(\d+)/, "($1) $2");
          } else {
            tel = tel.replace(/(\d+)/, "($1");
          }

          this.form.celular = tel;
        },

      cadastrarPaciente() {

        const enviado = {
          nome_completo: this.form.nome_completo,
          data_nascimento: this.form.data_nascimento,
          documento: this.form.cpf.replace(/\D/g, ""),
          telefone: this.form.telefone.replace(/\D/g, ""),
          celular: this.form.celular.replace(/\D/g, ""),
        };

        fetch("http://127.0.0.1:8000/api/pacientes/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(enviado),
        })
          .then(async (response) => {
            if (!response.ok) {
              const data = await response.json().catch(() => null);
              console.error("Erro da API:", data);
              alert("Erro ao cadastrar paciente");
              return;
            }

            this.mensagemSucesso = "Paciente cadastrado com sucesso!";

            this.form = {
              nome_completo: "",
              data_nascimento: "",
              cpf: "",
              telefone: "",
              celular: "",
            };
          })
          .catch((err) => console.error("Erro inesperado:", err));
      },
  },
  };
</script>


<style scoped>

  /* Caixa do formulário */
  .page {
    max-width: 1100px;
    width: 100%;
    margin: 0 auto;
    padding: 25px;
    background: rgba(56, 115, 155, 0.15); 
    border-radius: 12px;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  }

  /* Título */
  h1 { 
    text-align: center;
    margin-bottom: 20px;
    font-size: 28px;
    font-weight: bold;
    color: #0f6a7a; 
  }

  /* Estrutura do formulário */
  form {
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  /* Grupos dos campos */
  .form-group {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  /* Labels */
  .form-group label {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
    color: #0f6a7a;
  }

  /* Inputs */
  .form-group input,
  .form-group select {
    padding: 10px;
    border-radius: 6px;
    border: 2px solid #c8d7df;
    outline: none;
    font-size: 14px;
    background: #fff;
  }

  /* Foco dos campos de input ao clicar neles */
  .form-group input:focus,
  .form-group select:focus {
    border-color: #0f6a7a; 
    box-shadow: 0 0 5px rgba(15,106,122,0.4);
  }

  /* Texto "Opcional" */
  .info-opcional {
    font-size: 12px;
    color: #555;
    margin-top: 3px;
  }

  /* Botão Salvar */
  button {
    background-color: #0f6a7a;
    color: #ffffff;
    padding: 12px;
    border-radius: 10px;
    cursor: pointer;
    border: none;
    font-size: 16px;
    font-weight: bold;
    margin-top: 12px;
    transition: 0.3s;
  }
  button:hover {
    background-color: #0a4b56;
  }

  /* Mensagem de Sucesso */
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
