
# 🎓 Trabalho Final: Sistema de Gerenciamento de Inventário com Testes Automatizados

## 📘 Apresentação do Problema

Pequenos comércios enfrentam desafios na organização e controle do seu estoque. 
Produtos podem ser perdidos por falta de controle de validade, ruptura de estoque ou 
falta de atualização no registro de entrada e saída de mercadorias.

Este trabalho propõe o desenvolvimento de uma API REST simples, com foco em boas práticas 
de desenvolvimento e **Test-Driven Development (TDD)**, para gerenciar o inventário de 
produtos de uma loja ou armazém.

---

## 🎯 Objetivo Geral

Desenvolver uma aplicação backend com **Python e Flask**, usando TDD, que permita:

- Cadastrar e atualizar produtos
- Consultar e listar o estoque
- Registrar entradas e saídas de mercadorias
- Acompanhar o nível de estoque de cada item

---

## 📋 Requisitos do Sistema

### 🧱 Funcionalidades Obrigatórias

1. **Cadastro de produto**
   - Campos: `nome`, `categoria`, `quantidade_inicial`, `preco_unitario`
   - Restrições: `quantidade` ≥ 0, `preco` > 0

2. **Listagem de produtos**
   - Exibir todos os produtos com seus dados
   - Suporte a filtros por nome ou categoria (via query string)

3. **Consulta de produto por ID**
   - Retorna os dados completos de um produto específico

4. **Atualização de produto**
   - Permite atualizar nome, categoria ou preço unitário

5. **Operações de estoque**
   - Entrada: aumenta quantidade disponível
   - Saída: reduz quantidade (sem permitir estoque negativo)

6. **Remoção de produto**
   - Permite excluir um item do inventário

---

### 🧪 Requisitos de Testes

- Aplicar **TDD** no desenvolvimento das rotas
- Criar casos de teste unitário com `unittest` ou `pytest`
- Testar todos os endpoints com múltiplos cenários:
  - Sucesso
  - Erro de validação
  - Requisições inválidas
  - Operações com estoque zerado ou negativo

---

## ✅ Requisitos Técnicos

- Linguagem: Python 3.8+
- Framework: Flask
- Persistência: In-Memory (lista ou dicionário Python)
  - Opcional: persistência com arquivo `.json` ou SQLite
- Organização em módulos: `app.py`, `models.py`, `routes.py`, `tests/`

---

## 📦 Entrega

O pacote final deve conter:

- Código-fonte com estrutura organizada
- Casos de teste automatizados
- Instruções de execução (`README.md`)
- Opcional: script `run.sh` para setup automatizado

---

## 🧠 Sugestões de Expansão

- Autenticação (token ou login simples)
- Geração de relatórios (CSV)
- Interface com Flask-Admin ou Streamlit

---


## 🗂️ Organização de Módulos

### 📌 `app.py` – Inicialização da aplicação

Responsável por:

* Criar a instância `Flask`
* Importar e registrar as rotas (via *blueprints*, se desejar)
* Iniciar o servidor (em modo de desenvolvimento)

**Exemplo:**

```python
from flask import Flask
from routes import inventario_routes

app = Flask(__name__)
app.register_blueprint(inventario_routes)

if __name__ == "__main__":
    app.run(debug=True)
```

---

### 📌 `routes.py` – Definição das rotas da API

Responsável por:

* Declarar as rotas REST (`/produtos`, `/produtos/<id>`, etc.)
* Chamar as funções do módulo `models.py` para tratar a lógica
* Lidar com entrada/saída HTTP (parâmetros, JSON, status code)

**Exemplo:**

```python
from flask import Blueprint, jsonify, request
from models import criar_produto, listar_produtos

inventario_routes = Blueprint("inventario", __name__)

@inventario_routes.route("/produtos", methods=["GET"])
def rota_listar():
    return jsonify(listar_produtos())

@inventario_routes.route("/produtos", methods=["POST"])
def rota_criar():
    dados = request.get_json()
    produto = criar_produto(dados)
    return jsonify(produto), 201
```

---

### 📌 `models.py` – Lógica de negócio e manipulação de dados

Responsável por:

* Armazenar e manipular os dados do inventário
* Implementar funções como:

  * `criar_produto(dados)`
  * `listar_produtos()`
  * `obter_produto_por_id(id)`
  * `remover_produto(id)`
  * `entrada_estoque(id, qtd)`
  * `saida_estoque(id, qtd)`
* Garantir as regras de negócio (ex: não permitir estoque negativo)

**Exemplo:**

```python
estoque = []
proximo_id = 1

def criar_produto(dados):
    global proximo_id
    produto = {"id": proximo_id, **dados}
    estoque.append(produto)
    proximo_id += 1
    return produto

def listar_produtos():
    return estoque
```

---

### 📁 `tests/` – Testes automatizados

Responsável por:

* Conter todos os testes do projeto, organizados em arquivos como:

  * `test_produtos.py` – testa as rotas e funcionalidades principais
* Utilizar `unittest` ou `pytest`
* Cobrir todos os fluxos esperados e erros

**Exemplo:**

```python
import unittest
from app import app

class TestEstoqueAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_listar_produtos(self):
        response = self.client.get("/produtos")
        self.assertEqual(response.status_code, 200)
```

---

## ✅ Benefícios dessa organização

* **Separa responsabilidades** claramente
* Facilita a **manutenção** e **testabilidade**
* Permite reuso da lógica (`models.py`) em outros contextos (ex: CLI, GUI)
* Escala facilmente para projetos maiores

---
## 📅 Prazo

- Entrega até: 06/06/2025

Bom trabalho! 💪📦📊
