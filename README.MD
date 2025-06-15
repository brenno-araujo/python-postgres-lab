# Projeto Python + PostgreSQL com Docker

Este projeto é uma aplicação Python que utiliza PostgreSQL como banco de dados, orquestrados via Docker e Docker Compose para facilitar o desenvolvimento e deploy.

---

## Pré-requisitos

- Docker instalado: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose instalado (já vem embutido em versões recentes do Docker)

---

## Como usar

### 1. Clone este repositório

```bash
git clone https://github.com/brenno-araujo/python-postgres-lab.git
```

### 2. Inicie os serviços

```bash
docker-compose up -d
```

### 3. Acesse a aplicação

```bash
http://localhost:8001/health
```

### 4. Parar os serviços

```bash
docker-compose down
```

### 5. Acessar o shell do container

```bash
docker exec -it study-web-web-1 bash
```



