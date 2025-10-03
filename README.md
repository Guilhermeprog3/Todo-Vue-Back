# 📌 Todo-Vue-Back

Este é o **backend** para uma aplicação de lista de tarefas (**To-Do
List**), construído com **FastAPI** e **SQLAlchemy**.\
Ele fornece uma **API RESTful** para gerenciar **usuários** e
**tarefas**, incluindo autenticação JWT e operações CRUD.

------------------------------------------------------------------------

## 🚀 Funcionalidades

### 🔐 Autenticação de Usuário

-   Registro de novos usuários.
-   Login com **JWT (JSON Web Tokens)** para autenticação.

### ✅ Gerenciamento de Tarefas

-   Criar novas tarefas.
-   Listar todas as tarefas de um usuário autenticado.
-   Atualizar os detalhes de uma tarefa.
-   Excluir uma tarefa.
-   Marcar como **concluída / não concluída**.

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   [FastAPI](https://fastapi.tiangolo.com/) → Framework web moderno e
    rápido.
-   [SQLAlchemy](https://www.sqlalchemy.org/) → ORM para manipulação do
    banco de dados.
-   [Pydantic](https://docs.pydantic.dev/) → Validação de dados.
-   [Python-JOSE](https://python-jose.readthedocs.io/en/latest/) →
    Manipulação de **JWT**.
-   [Passlib](https://passlib.readthedocs.io/) → Hashing seguro de
    senhas.
-   [SQLite](https://www.sqlite.org/index.html) → Banco de dados
    utilizado.

------------------------------------------------------------------------

## 📡 Endpoints da API

### 🔐 Autenticação

-   **POST** `/users/` → Criar um novo usuário.\
-   **POST** `/token` → Autenticar usuário e gerar token JWT.

### 📝 Tarefas

-   **POST** `/tasks/` → Criar nova tarefa.\
-   **GET** `/tasks/` → Listar todas as tarefas do usuário autenticado.\
-   **PUT** `/tasks/{task_id}` → Atualizar tarefa existente.\
-   **DELETE** `/tasks/{task_id}` → Excluir tarefa.\
-   **PATCH** `/tasks/{task_id}/toggle` → Alternar status (concluída/não
    concluída).

------------------------------------------------------------------------

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

``` bash
git clone <URL_DO_REPOSITORIO>
cd todo-vue-back
```

### 2️⃣ Criar e ativar ambiente virtual

``` bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Instalar dependências

``` bash
pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib bcrypt
```

### 4️⃣ Executar o servidor

``` bash
uvicorn main:app --reload
```

A API estará disponível em:\
👉 <http://127.0.0.1:8000>

------------------------------------------------------------------------

## 📖 Documentação Automática

O FastAPI gera documentação automática da API: - Swagger UI →
<http://127.0.0.1:8000/docs>\
- Redoc → <http://127.0.0.1:8000/redoc>

------------------------------------------------------------------------

## 📌 Próximos Passos

-   [ ] Adicionar testes automatizados com **Pytest**.\
-   [ ] Implementar refresh token.\
-   [ ] Configurar Docker para deploy.\
-   [ ] Integração com frontend Vue (Todo-Vue-Front).

------------------------------------------------------------------------

## 📝 Licença

Este projeto é distribuído sob a licença **MIT**.\
Sinta-se livre para usar e modificar conforme necessário.

------------------------------------------------------------------------

👨‍💻 Desenvolvido com ❤️ usando **FastAPI**.
