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

# Requisitos

- Python instalado
- Pip instalado

Verificar versões:

```bash
python --version
pip --version
```

---

# Instalação

## 1. Entrar na pasta do projeto

```bash
cd vidaflow_api
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

# Banco de Dados

O projeto utiliza SQLite.

O banco é criado automaticamente ao iniciar a API.

Arquivo:

```txt
instance/database.db
```

Caso queira resetar o banco:

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

### URL completa

```txt
http://127.0.0.1:5000/v1/status
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

### URL completa

```txt
http://127.0.0.1:5000/v1/users
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

### URL completa

```txt
http://127.0.0.1:5000/v1/login
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

# Testes

Recomendado utilizar:

- Postman
- Insomnia

---

# Possíveis Erros

---


## no such table

O banco ainda não foi criado corretamente.

Solução:

1. Feche o servidor

2. Delete:

```txt
instance/database.db
```

3. Rode novamente:

```bash
python run.py
```


---

# Objetivo do Projeto

Este projeto serve para treinamento de:

- APIs REST
- SQLAlchemy ORM
- JWT Authentication
- Arquitetura Flask
- Integração Mobile
- Backend para aplicações React Native
- WorldSkills Mobile Application Development

---

# Autor

Daniel Calebe
