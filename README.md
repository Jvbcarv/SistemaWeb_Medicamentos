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

**Passo a passo rodar o Backend (Django) no terminal:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Backend disponível em: http://127.0.0.1:8000/

**Passo a passo rodar o Frontend (Vue 3 + Vite)<br>**
Abra outro terminal na raiz do projeto:
```bash
cd frontend
npm install
npm run dev
```
Frontend disponível em: http://127.0.0.1:5173/

---
## Sistema funcionando

- Tela de cadastro de medicamentos:<br><br>
<img width="1170" height="625" alt="image" src="https://github.com/user-attachments/assets/7807a36b-0816-44a1-8eef-6275fd6fd3a6" /><br>
- Tela de listagem de medicamentos:<br><br>
<img width="1333" height="707" alt="image" src="https://github.com/user-attachments/assets/c5963ff8-b927-4da6-be1a-50d3a3d18dda" /><br>
- Tela de cadastro de pacientes:<br><br>
<img width="1322" height="719" alt="image" src="https://github.com/user-attachments/assets/af20fd38-30fd-4b43-80ec-3d4184b0850c" /><br>
- Tela de Registro de Uso/Retirada de medicamentos:<br><br>
<img width="1263" height="913" alt="image" src="https://github.com/user-attachments/assets/9ec20ff5-f73c-4471-bf71-b505cdb2548d" /><br>
- Tela de Listagem de Registros Ativos:<br><br><br>
<img width="1400" height="814" alt="image" src="https://github.com/user-attachments/assets/729d782e-c93c-438b-9825-4ae57c4353e1" />


