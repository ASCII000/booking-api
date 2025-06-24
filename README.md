# 🚀 Booking API - Sistema de Reservas

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12+-green.svg)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-0.0.24+-orange.svg)](https://sqlmodel.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/Poetry-Management-purple.svg)](https://python-poetry.org/)

## 📋 Sobre o Projeto

Sistema completo de gerenciamento de reservas desenvolvido com **FastAPI** e **SQLModel**, demonstrando habilidades avançadas em desenvolvimento de APIs REST, arquitetura limpa e boas práticas de engenharia de software.

### 🎯 Objetivo
Este projeto foi desenvolvido como **portfólio técnico** para demonstrar competências em:
- Desenvolvimento de APIs RESTful escaláveis
- Arquitetura de software limpa e modular
- Implementação de autenticação e autorização
- Testes automatizados com pytest
- Gerenciamento de dependências com Poetry
- Documentação técnica e boas práticas

## 🏗️ Arquitetura e Tecnologias

### Stack Tecnológica
- **Backend**: FastAPI (Python 3.11+)
- **ORM**: SQLModel (combinação de SQLAlchemy + Pydantic)
- **Banco de Dados**: SQLite (configurável para PostgreSQL/MySQL)
- **Autenticação**: JWT (PyJWT)
- **Testes**: pytest + httpx
- **Gerenciamento**: Poetry
- **Formatação**: Black
- **Documentação**: OpenAPI/Swagger automática

### 🏛️ Arquitetura do Projeto
```
src/
├── domain/           # Lógica de negócio
├── models/           # Modelos Pydantic/SQLModel
├── repositories/     # Camada de acesso a dados
├── routers/          # Endpoints da API
├── dependencies/     # Injeção de dependências
├── database/         # Configuração e modelos de BD
├── utils/            # Utilitários (segurança, etc.)
└── main.py          # Ponto de entrada da aplicação
```

## 🚀 Funcionalidades Implementadas

### ✅ Gestão de Recursos
- **CRUD completo** de recursos (salas, equipamentos, espaços)
- Validação de dados com Pydantic
- Upload e gerenciamento de imagens
- Sistema de preços por hora
- Controle de disponibilidade

### ✅ Sistema de Usuários
- **Cadastro e autenticação** de clientes
- Sistema de login com JWT
- Validação de email único
- Controle de saldo/balance
- Histórico de reservas

### ✅ Reservas e Transações
- Sistema de reservas com relacionamentos
- Controle de disponibilidade em tempo real
- Histórico de transações
- Validações de negócio

## 🔧 Configuração e Instalação

### Pré-requisitos
- Python 3.11+
- Poetry (gerenciador de dependências)

### Instalação

1. **Clone o repositório**
```bash
git clone <repository-url>
cd booking-api
```

2. **Instale as dependências**
```bash
poetry install
```

3. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. **Execute a aplicação**
```bash
# Usando Poetry
poetry run python -m src.main

# Ou usando o script
./scripts/run_api.bash
```

### 🧪 Executando os Testes
```bash
poetry run pytest
```

## 📚 Documentação da API

Após iniciar a aplicação, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints Principais

#### Recursos (`/v1/resources`)
- `GET /` - Listar todos os recursos
- `POST /` - Criar novo recurso
- `PUT /?resource_id={id}` - Editar recurso

#### Clientes (`/v1/clients`)
- `POST /` - Cadastrar novo cliente
- `POST /login` - Autenticação de cliente

## 🎯 Pontos Fortes do Projeto

### 💻 **Qualidade de Código**
- **Arquitetura limpa** com separação clara de responsabilidades
- **Injeção de dependências** para testabilidade
- **Type hints** em todo o código
- **Formatação automática** com Black
- **Linting** com pylint

### 🧪 **Testes e Qualidade**
- **Testes unitários** com pytest
- **Mocks** para isolamento de dependências
- **Fixtures** reutilizáveis
- **Cobertura de testes** para endpoints críticos

### 🔒 **Segurança**
- **Autenticação JWT** implementada
- **Validação de dados** com Pydantic
- **Sanitização** de inputs
- **Controle de acesso** por endpoints

### 📊 **Banco de Dados**
- **ORM moderno** (SQLModel)
- **Migrations** e versionamento de schema
- **Relacionamentos** bem definidos
- **Índices** para performance

### 🚀 **Performance e Escalabilidade**
- **Async/await** para operações I/O
- **Connection pooling** configurável
- **Caching** preparado para implementação
- **Rate limiting** ready

## 🎨 Padrões e Boas Práticas

### ✅ **SOLID Principles**
- **Single Responsibility**: Cada classe tem uma responsabilidade
- **Open/Closed**: Extensível sem modificação
- **Dependency Inversion**: Dependências injetadas

### ✅ **Clean Architecture**
- **Domain Layer**: Lógica de negócio isolada
- **Repository Pattern**: Abstração de acesso a dados
- **Service Layer**: Orquestração de operações

### ✅ **API Design**
- **RESTful** endpoints
- **Versionamento** de API (/v1/)
- **Status codes** apropriados
- **Error handling** consistente

## 🔮 Próximos Passos e Melhorias

### 🚀 **Funcionalidades Futuras**
- [ ] Sistema de notificações
- [ ] Dashboard administrativo
- [ ] Relatórios e analytics
- [ ] Integração com pagamentos
- [ ] API rate limiting
- [ ] Cache com Redis

### 🛠️ **Melhorias Técnicas**
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Monitoramento com Prometheus
- [ ] Logs estruturados
- [ ] Documentação com Sphinx

## 👨‍💻 Sobre o Desenvolvedor

**Emerson Silva** - Desenvolvedor Backend Python

### 🎯 **Competências Demonstradas**
- **FastAPI** e desenvolvimento de APIs REST
- **SQLModel/SQLAlchemy** para ORM
- **Arquitetura de software** limpa e escalável
- **Testes automatizados** e TDD
- **DevOps** e boas práticas de desenvolvimento
- **Documentação** técnica e APIs

---

## 📄 Licença

Este projeto é open source e está disponível sob a licença MIT.

---

**⭐ Se este projeto foi útil, considere dar uma estrela no repositório!**