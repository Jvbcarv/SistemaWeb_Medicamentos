<template>
  <div class="page">
    <h1> Pacientes Cadastrados </h1>

    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th> Nome completo </th>
            <th> CPF </th>
            <th> Data de Nascimento </th>
            <th> Telefone </th>
            <th> Celular </th>
            <th> Ações </th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="pac in pacientes" :key="pac.id">
            <td>{{ pac.nome_completo }}</td>
            <td>{{ formatarCPF(pac.documento) }}</td>
            <td>{{ formatarData(pac.data_nascimento) }}</td>
            <td>{{ formatarTelefone(pac.telefone) }}</td>
            <td>{{ formatarCelular(pac.celular) }}</td>
            <td>
              <button @click="editarPaciente(pac.id)"> Editar </button> 
              <button @click="excluirPaciente(pac.id)"> Excluir </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>


<script>
  export default {
    name: "PacientesView",

    data() {
      return {
        pacientes: [],
      };
    },

    mounted() {
      fetch("http://127.0.0.1:8000/api/pacientes/")
        .then((response) => response.json())
        .then((data) => {
          this.pacientes = data;
        })
        .catch(() => alert("Erro ao carregar pacientes cadastrados."));
    },

    methods: {
      formatarData(data) {
        return new Date(data).toLocaleDateString("pt-BR");
      },

      formatarCPF(cpf) {
        if (!cpf) return "";
        cpf = cpf.replace(/\D/g, "");
        return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
      },

      formatarTelefone(tel) {
        if (!tel) return "Não informado";
        tel = tel.replace(/\D/g, "");
        return tel.replace(/(\d{2})(\d{4})(\d{4})/, "($1) $2-$3");
      },

      formatarCelular(tel) {
        if (!tel) return "Não informado";
        tel = tel.replace(/\D/g, "");
        return tel.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
      },

      editarPaciente(id) {
        this.$router.push(`/editar-paciente/${id}`);
      },

      excluirPaciente(id) {
        if (!confirm("Tem certeza que deseja excluir este paciente?")) return;

        fetch(`http://127.0.0.1:8000/api/pacientes/${id}/`, {
          method: "DELETE",
        })
          .then((response) => {
            if (!response.ok) {
              alert("Erro ao excluir paciente");
              return;
            }

            // Remove da lista sem recarregar a página
            this.pacientes = this.pacientes.filter((p) => p.id !== id);
          })
          .catch(() => alert("Erro ao excluir paciente"));
      },
    },
  };
</script>


<style scoped>

  /* Caixa da Tabela */
  .page {
    width: 140%;  /*largura da tabela*/
    margin: 0 auto;
    padding: 20px;
    background: rgba(56, 115, 155, 0.15);
    border-radius: 12px;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  }
  table {
    width: 100%;
  }

  /* Título */
  h1 {
    text-align: center;
    margin-bottom: 20px;
    font-size: 28px;
    color: #0f6a7a;
  }

  /* Cabeçalho */
  thead th {
    background-color: rgba(15, 106, 122, 0.85);
    color: #ffffff;
    padding: 14px;
    font-size: 15px;
    text-align: center;
    font-weight: bold;
    border: none;
  }

  /* Células da tabela */
  tbody td {
    background-color: #ffffff;
    color: #000000;
    padding: 15px;
    border-bottom: 1px solid #dcdcdc;
    text-align: center;
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

  /* responsividade da tabela */
  .table-responsive {
    width: 100%;
    overflow-x: auto;
  }

  /* Evita que a tabela quebre */
  .table-responsive table {
    min-width: 700px;
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
  }
</style>




