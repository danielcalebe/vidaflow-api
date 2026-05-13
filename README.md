# VidaFlow API

API REST construída com Flask + SQLAlchemy para treinamento de desenvolvimento backend, autenticação JWT e integração com aplicações mobile/web.

---

# Tecnologias

- Python 3.12+
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Flask JWT Extended
- SQLite

---

# Estrutura do Projeto

```bash
vidaflow_api/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── extensions.py
│
├── instance/
│   └── database.db
│
├── requirements.txt
├── run.py
└── README.md
```

---

# Instalação

## 1. Clonar projeto

```bash
git clone URL_DO_REPOSITORIO
```

ou apenas copiar a pasta do projeto.

---

## 2. Entrar na pasta

```bash
cd vidaflow_api
```

---

# Ambiente Virtual (Opcional)

## Windows

```powershell
python -m venv venv
```

Ativar:

```powershell
venv\Scripts\activate
```

---

# Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# Executar API

```bash
python run.py
```

Servidor:

```txt
http://127.0.0.1:5000
```

---

# Criar Banco de Dados

O projeto cria automaticamente as tabelas ao iniciar.

Caso necessário apagar tudo:

1. Delete:

```txt
instance/database.db
```

2. Rode novamente:

```bash
python run.py
```

---

# Rotas Disponíveis

---

## STATUS API

### GET

```http
/v1/status
```

### Resposta

```json
{
    "message": "API ONLINE"
}
```

---

# CRIAR USUÁRIO

### POST

```http
/v1/users
```

### Body

```json
{
    "name": "Daniel",
    "email": "dan@gmail.com",
    "password": "123"
}
```

### Resposta

```json
{
    "message": "Usuário criado"
}
```

---

# LOGIN

### POST

```http
/v1/login
```

### Body

```json
{
    "email": "dan@gmail.com",
    "password": "123"
}
```

### Resposta

```json
{
    "access_token": "TOKEN_JWT"
}
```

---

# Rotas Futuras

- CRUD de tarefas
- Upload de imagem
- Refresh token
- Recuperação de senha
- Sistema de permissões
- Notificações
- Logs
- Dashboard admin

---

# Testes

Recomendado usar:

- Postman
- Insomnia

---

# Possíveis Erros

## 404 NOT FOUND

Você provavelmente usou URL errada.

Exemplo correto:

```txt
http://127.0.0.1:5000/v1/status
```

---

## no such table

O banco ainda não foi criado.

Solução:

```bash
python run.py
```

---

## ImportError

Verifique:

- nomes dos arquivos
- imports
- __init__.py nas pastas

---

# Objetivo do Projeto

Este projeto serve para treinamento de:

- APIs REST
- SQLAlchemy ORM
- JWT Authentication
- Arquitetura Flask
- Integração Mobile
- WorldSkills Mobile Application Development

---

# Autor

Daniel Calebe