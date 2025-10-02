Todo-Vue-Back
Este é o backend para uma aplicação de lista de tarefas (To-Do List), construído com FastAPI e SQLAlchemy. Ele fornece uma API RESTful para gerenciar usuários e tarefas, incluindo autenticação de usuário e operações CRUD para tarefas.

Funcionalidades
Autenticação de Usuário:

Registro de novos usuários.

Login de usuários com JWT (JSON Web Tokens) para autenticação.

Gerenciamento de Tarefas:

Criar novas tarefas.

Ler todas as tarefas de um usuário.

Atualizar os detalhes de uma tarefa.

Excluir uma tarefa.

Marcar uma tarefa como concluída/não concluída.

Tecnologias Utilizadas
FastAPI: Um moderno e rápido framework web para Python para construir APIs.

SQLAlchemy: Um ORM (Object Relational Mapper) para interagir com o banco de dados.

Pydantic: Para validação de dados.

JOSE: Para manipulação de JWT (JSON Web Tokens).

Passlib: Para hashing de senhas.

SQLite: O banco de dados utilizado neste projeto.

Endpoints da API
Autenticação
POST /users/: Cria um novo usuário.

POST /token: Autentica um usuário e retorna um token de acesso.

Tarefas
POST /tasks/: Cria uma nova tarefa.

GET /tasks/: Retorna a lista de tarefas do usuário autenticado.

PUT /tasks/{task_id}: Atualiza uma tarefa existente.

DELETE /tasks/{task_id}: Exclui uma tarefa.

PATCH /tasks/{task_id}/toggle: Alterna o status de conclusão de uma tarefa.

Como Executar o Projeto
Clone o repositório:

Bash

git clone <URL do repositório>
cd todo-vue-back
Crie e ative um ambiente virtual:

Bash

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:

Bash

pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib bcrypt
Execute o servidor:

Bash

uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.