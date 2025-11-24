<template>
  <div class="page">
    <h1> Listagem de Medicamentos Cadastrados </h1><br>

    <!-- Filtro-->
    <label>Filtrar por Categoria:</label>
    <select v-model="categoriaFiltro">
      <option value="">Todas</option>
      <option v-for="item in categoriasUnicas" :key="item" :value="item">
        {{ item }}
      </option>
    </select>
    <br><br>

    <!-- Tabela -->
    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th> Medicamento </th>
            <th> Categoria </th>
            <th> Apresentação </th>
            <th> Ações </th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="item in medicamentosFiltrados" :key="item.id">
            <td>{{ item.nome }}</td>
            <td>{{ item.categoria_nome }}</td>
            <td>{{ item.apresentacao }}</td>
            <td>
              <button @click="editarMedicamento(item.id)"> Editar </button> 
              <button @click="excluirMedicamento(item.id)"> Excluir </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    </div>
</template>


<script>
  export default {
    name: "MedicamentosView",

    data() {
      return {
        medicamentos: [],
        categoriaFiltro: ""
      };
    },

    computed: {
      medicamentosFiltrados() {
        if (!this.categoriaFiltro) return this.medicamentos;
        return this.medicamentos.filter(
          m => m.categoria_nome === this.categoriaFiltro
        );
      },

      categoriasUnicas() {
        const categorias = this.medicamentos.map(m => m.categoria_nome);
        return [...new Set(categorias)];
      }
    },

    mounted() {
      fetch("http://127.0.0.1:8000/api/medicamentos/")
        .then((response) => response.json())
        .then((data) => {
          this.medicamentos = data;
        })
        .catch(() => alert("Erro ao carregar medicamentos"));
    },

    methods: {
      editarMedicamento(id) {
        this.$router.push(`/editar-medicamento/${id}`);
      },

      excluirMedicamento(id) {
        if (!confirm("Tem certeza que deseja excluir este medicamento?")) return;

        fetch(`http://127.0.0.1:8000/api/medicamentos/${id}/`, {
          method: "DELETE",
        })
          .then((response) => {
            if (!response.ok) {
              alert("Erro ao excluir medicamento!");
              return;
            }

            this.medicamentos = this.medicamentos.filter((m) => m.id !== id);
          })
          .catch(() => alert("Erro ao excluir medicamento!"));
      },
    },
  };
</script>


<style scoped>

  /* Caixa da tabela*/
  .page {
    max-width: 1100px; /*largura da tabela */
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
    margin-bottom: 20px;
    font-size: 28px;
    color: #0f6a7a;
  }

  /* estilização do filtro */
  label {
    font-size: 16px;
    font-weight: 600;
    color: #0f6a7a;
    margin-right: 10px;
  }
  select {
    padding: 8px 12px;
    border-radius: 8px;
    border: 2px solid rgba(15, 106, 122, 0.35);
    background-color: #ffffff;
    font-size: 14px;
    color: #0f6a7a;
    cursor: pointer;
    outline: none;
    transition: 0.2s;
  }
  /* Hover e focus do filtro */
  select:hover,
  select:focus {
    border-color: #0f6a7a;
    box-shadow: 0 0 4px #0f6a7a;
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
  }

  /* Hover da linha */
  tbody tr:hover {
    background-color: #eef4ff;
    transition: 0.2s;
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
    margin: 5px auto; /* separação os botões */
    display: block;  /* um botão embaixo do outro */
    transition: 0.3s;
  }

  tbody td button:hover {
    background-color: #0a4b56;
  }

  /* Responsividade da Tabela */

    .table-responsive {
      width: 100%;
      overflow-x: auto;
    }
    .table-responsive table {
      min-width: 600px;
    }

    /* Ajuste para telas pequenas */
    @media (max-width: 600px) {
      h1 {
        font-size: 22px;
      }

      select {
        width: 100%;
        margin-top: 10px;
      }

      .page {
        padding: 10px;
      }

      thead th, tbody td {
        font-size: 13px;
        padding: 10px;
      }

      tbody td button {
        width: 100%;
      }
    }
</style>

