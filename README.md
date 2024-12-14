# Gerenciamento de Tarefas (To-Do List)

Bem-vindo ao projeto **To-Do List**, uma aplicação desenvolvida em Django REST Framework, projetada para gerenciar tarefas com funcionalidades avançadas de CRUD, autenticação JWT e filtragem. Este documento fornece instruções detalhadas para rodar o projeto, explica sua arquitetura e justifica as principais decisões de design.

## Índice
1. [Visão Geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [Instalação e Configuração](#instalação-e-configuração)
4. [Comandos Importantes](#comandos-importantes)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Decisões de Design](#decisões-de-design)
7. [Testes](#testes)
8. [Autor](#autor)

---

## Visão Geral

A aplicação To-Do List é uma solução robusta para gerenciar tarefas. Desenvolvida com **Django REST Framework**, a aplicação utiliza práticas modernas de desenvolvimento, incluindo:

- **CRUD Completo** para tarefas.
- **Autenticação JWT**.
- **Filtros e Paginação** para melhor gerenciamento de dados.
- **Testes Automatizados** utilizando `pytest`.
- **Dockerização** para fácil implantação e execução.

![Django Logo](https://static.djangoproject.com/img/logos/django-logo-negative.png)

---

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.9+
- Docker e Docker Compose
- Git

---

## Instalação e Configuração

### Clonando o Repositório
```bash
git clone https://github.com/seu-repositorio/todo-list-backend.git
cd todo-list-backend
```

### Configurando Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto e configure as seguintes variáveis:
```env
# Banco de Dados
POSTGRES_DB=todo_db
POSTGRES_USER=todo_user
POSTGRES_PASSWORD=todo_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Django
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=*
```

### Iniciando com Docker

1. Construa e inicie os containers:
```bash
docker-compose up --build
```

2. Acesse a aplicação no navegador em:
```
http://localhost:8000
```

---

## Comandos Importantes

### Backend
Esses comandos estão automaticos dentro do Docker no arquivo `entrypoint.sh`

- Aplicar migrações:
```bash
docker-compose exec web python manage.py migrate
```

- Carregar fixtures (dados iniciais):
```bash
docker-compose exec web python manage.py loaddata tasks/fixtures/tasks.json
```

### Testes
- Rodar testes automatizados:
```bash
docker-compose exec web pytest
```

---

## Estrutura do Projeto

```
todo_list_backend/
├── config/                # Configurações do projeto Django
├── tasks/                 # Aplicativo principal
│   ├── fixtures           # Seeder do modelo Task
│   ├── models.py          # Definição do modelo Task
│   ├── serializers.py     # Serializadores
│   ├── views.py           # ViewSets e lógica de negócio
│   ├── urls.py            # Rotas específicas do app
│   ├── tests/             # Testes automatizados
├── manage.py              # Utilitário do Django
├── docker-compose.yml     # Configuração do Docker Compose
├── requirements.txt       # Dependências do Python
├── README.md              # Documentação do projeto
```

---

## Decisões de Design

1. **Autenticação JWT**:
   - Optamos pelo Djoser para integrar endpoints JWT de forma fácil e segura.

2. **Filtros Personalizados**:
   - Implementamos filtros para busca exata ou parcial por título, oferecendo flexibilidade ao usuário.

3. **Testes Automatizados**:
   - `pytest` foi escolhido para garantir qualidade no código e facilitar a manutenção.

4. **Paginação**:
   - Paginação implementada com `PageNumberPagination`, configurável via query params.

5. **Dockerização**:
   - Todo o projeto foi dockerizado para garantir compatibilidade de ambiente em diferentes máquinas.

---

## Testes

Testes automatizados garantem a qualidade da aplicação. Eles incluem:

1. **Testes de CRUD**:
   - Criação, leitura, atualização e exclusão de tarefas.

2. **Testes de Filtros e Busca**:
   - Busca por título, filtragem por status concluído e paginação.


### Rodando os Testes

Execute os testes com o comando:
```bash
docker-compose exec web pytest
```

---

