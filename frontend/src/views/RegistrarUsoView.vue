<template>

  <div class="page">

    <h1>Registro de Retirada de Medicamento</h1>

    <form @submit.prevent="registrarUso">

    <h2> Retirada do medicamento </h2>

      <div class="form-group">
        <label> Paciente: </label>
        <select v-model="form.paciente" required>
          <option value=""> Selecione um paciente </option>
          <option v-for="p in pacientes" :key="p.id" :value="p.id">
            {{ p.nome_completo }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label> Medicamento retirado: </label>
        <select v-model="form.medicamento" required>
          <option value="">Selecione um medicamento</option>
          <option v-for="m in medicamentos" :key="m.id" :value="m.id">
            {{ m.nome }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label> Data da retirada: </label>
        <input type="date" v-model="form.data_retirada" required />
      </div>

      <div class="form-group">
        <label> Quantidade retirada: </label>
        <input type="text" v-model="form.quantidade" placeholder="Exemplo: 1 caixa." required/>
      </div>

      <h2> Uso do medicamento </h2>

      <div class="form-group">
        <label> Período de uso: </label>
        <input type="text" v-model="form.periodo_uso" placeholder="Exemplo: 3 meses." />
      </div>
    
      <h2> Encerramento do vínculo do paciente </h2>

      <div class="form-group">
        <label> Data final de uso do medicamento: </label>
        <input type="date" v-model="form.data_final" />
      </div>

      <button type="submit"> Registrar </button>
    </form>

    <p v-if="mensagemSucesso" class="sucesso">{{ mensagemSucesso }}</p>

  </div>

</template>

<script>
  export default {
    name: "RegistrarUsoView",
    data() {
      return {
        form: {
          paciente: "",
          medicamento: "",
          data_retirada: "",
          quantidade: "",
          periodo_uso: "",
          data_final: "",
        },
        pacientes: [],
        medicamentos: [],
        mensagemSucesso: "",
      };
    },
    mounted() {
      fetch("http://127.0.0.1:8000/api/pacientes/")
        .then(res => res.json())
        .then(data => this.pacientes = data);

      fetch("http://127.0.0.1:8000/api/medicamentos/")
        .then(res => res.json())
        .then(data => this.medicamentos = data);
    },
    methods: {
      registrarUso() {
        fetch("http://127.0.0.1:8000/api/registros-uso/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            paciente_id: this.form.paciente,
            medicamento_id: this.form.medicamento,
            quantidade: this.form.quantidade,
            data_retirada: this.form.data_retirada,
            periodo_uso: this.form.periodo_uso,
            data_final: this.form.data_final
          }),
        })
        .then(async response => {
          const data = await response.json();
          console.log(data);

          if (!response.ok) {
            alert("Erro ao registrar uso!");
            return;
          }

          this.mensagemSucesso = "Retirada registrada com sucesso!";

          this.form = {
            paciente: "",
            medicamento: "",
            data_retirada: "",
            quantidade: "",
            periodo_uso: "",
            data_final: "",
          };
        })
        .catch(() => alert("Erro na conexão com a API"));
      }
    }
  };
</script>


<style scoped>

  /* Caixa geral da página */
  .page {
    max-width: 500px;
    margin: 20px auto;
    padding: 12px 28px;
    background: linear-gradient(180deg, rgba(255,255,255,0.35), rgba(255,255,255,0.15));
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.4);
  }

  /* Título principal */
  h1 { 
    text-align: center;
    margin-bottom: 1px;
    font-size: 32px;
    font-weight: bold;
    color: #0f6a7a;
  }

  /* subtítulos das seções - h2 */
  h2 {
    font-size: 20px;
    margin-top: 25px;
    margin-bottom: 12px;
    color: #0f6a7a;
    border-bottom: 2px solid #0f6a7a;
    padding-bottom: 4px;
  }

  /* Estrutura dos campos */
  form {
    display: flex;
    flex-direction: column;
    gap: 1px; /* altura do espaçamento entre os campos*/
  }

  .form-group {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  /* Labels */
  .form-group label {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 6px;
    color: #0f6a7a;
  }

  /* Inputs padrão */
  .form-group input,
  .form-group select,
  .form-group textarea {
    padding: 12px;
    height: 45px;
    border-radius: 10px;
    border: 2px solid rgba(0, 0, 0, 0.15);
    outline: none;
    font-size: 15px;
    background: #ffffff;
  }

  /* Foco ao clicar nos campos de input*/
  .form-group input:focus,
  .form-group select:focus,
  .form-group textarea:focus {
    border-color: #0f6a7a;
    box-shadow: 0 0 8px rgba(15,106,122,0.35);
  }

  /* Botão */
  button {
    background-color: #0f6a7a;
    color: #ffffff;
    padding: 14px;
    border-radius: 10px;
    cursor: pointer;
    border: none;
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
    transition: 0.25s;
    width: 100%;
  }

  button:hover {
    background-color: #0c5865;
    transform: scale(1.02);
  }

  /* Mensagem de sucesso */
  .sucesso {
    color: #008f3f;
    font-size: 17px;
    margin-top: 18px;
    text-align: center;
    font-weight: bold;
  }
</style>

