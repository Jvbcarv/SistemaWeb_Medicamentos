<template>
  <div class="page">
    <h1> Registros Ativos </h1>

    <div class="table-responsive">
    <table class="tabela-registros">
      <thead>
        <tr>
          <th> Paciente </th>
          <th> Medicamento </th>
          <th> Período de Uso </th>
          <th> Data da Retirada </th>
          <th> Quantidade retirada </th>
          <th> Data final de uso </th>
          <th> Status </th>
          <th> Ação </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in registros" :key="item.id">
          <td>{{ item.paciente?.nome_completo }}</td>
          <td>{{ item.medicamento?.nome }}</td>
          <td>{{ item.periodo_uso }}</td>
          <td>{{ formatarData(item.data_retirada) }}</td>
          <td>{{ item.quantidade }}</td>
          <td>{{ formatarData(item.data_final) }}</td>

          <td :class="statusClasse(item)">
            {{ statusLabel(item) }}
          </td>

          <td>
            <button
              v-if="statusLabel(item) === 'Ativo'"
              @click="inativar(item.id)"
              class="btn-inativar"
            >
              Inativar
            </button>

            <span v-else class="inativo-label">✔ Inativo</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

    <p class="regra-status">
    O status do registro é determinado pela <strong>Data final de uso do medicamento</strong>:
    <br><br>
    • Quando a data final ainda não chegou ou está vazia → o registro é considerado <strong class="status-ativo">Ativo</strong><br>
    Isso significa que o paciente poderá solicitar mais medicamentos, de acordo com o Período de Uso do medicamento informado na receita (Exemplo: 1 ano) - Período cadastrado nesta tabela.<br><br>
    
    • Quando a data final é igual ou anterior à data de hoje → o registro é marcado automaticamente como <strong class="status-inativo">Inativo</strong>.<br><br>
    Obs.: o registro pode ser inativado manualmente, para casos por exemplo onde o paciente não retorne para solicitar mais medicamentos, mesmo não vencendo a data final do período de uso do medicamento.<br><br>
  </p>

  </div>
</template>

<script>
  export default {
    name: "RegistrosAtivosView",
    data() {
      return {
        registros: [],
      };
    },
    mounted() {
      this.buscarRegistros();
    },
    methods: {
      buscarRegistros() {
        fetch("http://127.0.0.1:8000/api/registros-uso/lista/ativos/")
          .then(res => res.json())
          .then(data => this.registros = data)
          .catch(() => alert("Erro ao carregar registros!"));
      },

      formatarData(data) {
        if (!data) return "";
        return new Date(data).toLocaleDateString("pt-BR");
      },

      statusLabel(item) {
        if (!item.data_final) return "Ativo";

        const hoje = new Date();
        const fim = new Date(item.data_final);

        return fim >= hoje ? "Ativo" : "Inativo";
      },

      statusClasse(item) {
        return this.statusLabel(item) === "Ativo" ? "status-ativo" : "status-inativo";
      },

      inativar(id) {
        const hoje = new Date().toISOString().split("T")[0];

        fetch(`http://127.0.0.1:8000/api/registros-uso/${id}/`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ data_final: hoje }),
        })
        .then(() => this.buscarRegistros())
        .catch(() => alert("Erro ao inativar!"));
      }
    }
  };
</script>

<style scoped>

  /* Caixa da tabela*/
  .page {
    max-width: 1000px; /*largura da tabela */
    width: 100%;
    margin: 0 auto;
    padding: 20px;
    background: rgba(56, 115, 155, 0.15);
    border-radius: 12px;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  }

  /* Título da tela */
  h1 {
    text-align: center;
    margin-bottom: 10px;
    font-size: 28px;
    color: #0f6a7a;
  }

  /* Tabela */
  .tabela-registros {
    width: 100%;
    border-collapse: collapse;
    border-radius: 12px;
    overflow: hidden;
  }

  /* Cabeçalho da tabela */
  thead th {
    background-color: rgba(15, 106, 122, 0.85); 
    color: #ffffff;
    padding: 14px;
    font-size: 15px;
    text-align: center;
    font-weight: bold;
    border: none;
  }

  /* Células */
  tbody td {
    background-color: #ffffff;
    color: #000000;
    padding: 15px;
    border-bottom: 1px solid #dcdcdc;
    text-align: center;
    font-size: 14px;
  }

  /* Hover da linha */
  tbody tr:hover {
    background-color: #eef4ff;
    transition: 0.2s;
  }

  /* Status visual */
  .status-ativo {
    font-weight: bold;
    color: #008f3f;
  }

  .status-inativo {
    font-weight: bold;
    color: #c92a2a;
  }

  /* Botões */
  tbody td button {
    background-color: #0f6a7a;
    color: #ffffff;
    border: none;
    padding: 8px 14px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 14px;
    width: 85px; 
    margin: 5px auto; 
    display: block;
    transition: 0.3s;
  }

  tbody td button:hover {
    background-color: #0a4b56;
  }

  /* Texto p/ Inativo */
  .inativo-label {
    color: #555;
    font-weight: bold;
  }

  /* texto abaixo da tabela*/
  .regra-status {
    margin-top: 20px;
    padding: 15px;
    background: rgba(255, 255, 255, 0.75);
    border-radius: 8px;
    font-size: 14px;
    color: #0a3d44;
    line-height: 1.6;
    border-left: 4px solid #0f6a7a;
  }

  /* responsividade */
  .table-responsive {
    width: 100%;
    overflow-x: auto;
  }

  .table-responsive table {
    min-width: 900px;
  }

  @media (max-width: 600px) {
    h1 {
      font-size: 22px;
    }

    .page {
      padding: 10px;
      width: 100%;
    }

    thead th,
    tbody td {
      font-size: 13px;
      padding: 10px;
    }

    tbody td button {
      width: 100%;
      font-size: 12px;
    }

    .regra-status {
      font-size: 12px;
      padding: 10px;
    }
  }
</style>
