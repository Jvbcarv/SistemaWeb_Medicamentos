##  Sistema de Gestão de Uso de Medicamentos:
Sistema web desenvolvido para auxiliar o controle de retirada e utilização de medicamentos por pacientes, contendo funcionalidades de cadastro, consulta e gerenciamento de registros ativos.
---
Objetivo do Sistema:
- Cadastrar pacientes.
- Cadastrar medicamentos.
- Listar medicamentos com filtro por categoria.
- Registrar retirada de medicamentos por pacientes.
- Visualizar registros ativos (uso contínuo).
- Editar e excluir cadastros.
---
## Tecnologias Utilizadas: 
Backend:
- **Python** 3.13.6
- **Django** 5.2.8
- Banco de dados: **SQLite** (padrão)

Frontend:
- **Vue.js** 3.5.24
- **Vite** 7.2.4
- HTML5 / CSS3 para estilização e responsividade

---
## Como Rodar o Projeto Localmente

Pré-requisitos - Instalação de dependências
- Python 3.13.6 instalado
- Node.js + npm instalados (Vue e dependências serão instaladas via `npm install`)
- Git instalado para clonar o projeto (para clonar o projeto)

```bash
Passo a passo rodar o Backend (Django) no terminal:

cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Backend disponível em: http://127.0.0.1:8000/

---------------------------------------------
Passo a passo rodar o Frontend (Vue 3 + Vite)
Abra outro terminal na raiz do projeto:

cd frontend
npm install
npm run dev
Frontend disponível em: http://127.0.0.1:5173/

