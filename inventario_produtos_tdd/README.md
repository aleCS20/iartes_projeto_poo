
# 📦 Trabalho Final: Sistema de Gerenciamento de Inventário com Testes Automatizados

Este projeto é um sistema simples de gerenciamento de estoque de produtos com API REST feita em Flask, utilizando armazenamento in-memory e testes automatizados com `unittest`.

---

## ▶️ Como executar o sistema

1. **Instale as dependências**:

```bash
pip install flask
```

2. **Execute o aplicativo Flask**:

```bash
python app.py
```

> A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✅ Endpoints disponíveis

- `GET    /produtos` — Listar todos os produtos  
- `POST   /produtos` — Criar um novo produto  
- `GET    /produtos/<id>` — Obter detalhes de um produto específico  
- `POST   /produtos/<id>/entrada` — Registrar entrada de estoque  
- `POST   /produtos/<id>/saida` — Registrar saída de estoque  
- `PUT    /produtos/<id>` — Atualizar nome, categoria ou preço unitário de um produto  
- `DELETE /produtos/<id>` — Remover um produto do estoque  

---

## 🧪 Como rodar os testes

1. **Ative o ambiente virtual**

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

2. **Execute os testes com o unittest**:

```bash
python -m unittest discover -s tests
```

> Também é possível utilizar o script `run_tests.bat` (Windows) para automatizar a execução.

---

## 🔬 Como testar com Postman

Você pode usar o **Postman** para testar facilmente todos os endpoints da API.

### 📁 Criar um produto (`POST /produtos`)

- **URL**: `http://localhost:5000/produtos`
- **Método**: POST
- **Body (raw JSON)**:
```json
{
  "nome": "Café",
  "categoria": "Bebidas",
  "quantidade_inicial": 20,
  "preco_unitario": 9.5
}
```

---

### 📋 Listar produtos (`GET /produtos`)

- **URL**: `http://localhost:5000/produtos`
- **Método**: GET

Você pode adicionar filtros:
- `?nome=cafe`
- `?categoria=bebidas`

---

### 📥 Entrada de estoque (`POST /produtos/<id>/entrada`)

- **URL**: `http://localhost:5000/produtos/1/entrada`
- **Body**:
```json
{
  "quantidade": 5
}
```

---

### 📤 Saída de estoque (`POST /produtos/<id>/saida`)

- **URL**: `http://localhost:5000/produtos/1/saida`
- **Body**:
```json
{
  "quantidade": 3
}
```

---

### ✏️ Atualizar produto (`PUT /produtos/<id>`)

- **URL**: `http://localhost:5000/produtos/1`
- **Body**:
```json
{
  "nome": "Café Torrado",
  "preco_unitario": 10.0
}
```

---

### 🗑️ Deletar produto (`DELETE /produtos/<id>`)

- **URL**: `http://localhost:5000/produtos/1`
- **Método**: DELETE
- **Body**: *(vazio)*

---

## 🗂️ Organização do Projeto

```
inventario_produtos_tdd/
├── app.py                  # Inicializa o app Flask
├── routes.py               # Define as rotas da API
├── models.py               # Lógica de negócio e estrutura dos dados
├── tests/
│   └── test_produtos.py    # Testes automatizados da API
├── README.md               # Instruções de uso do app para testes
├── requirements.txt        # arquivo com as bibliotecas necessárias do projeto
├── Tests Inventario Produtos.postman_collection.json  # arquivo .json de teste do Postman
```

---

## 🚀 Requisitos técnicos

- Python 3.8+
- Flask
- Testes com `unittest`
- Armazenamento em memória (lista Python)

---

## 📅 Entrega

Data limite: 06/06/2025  
Bom trabalho! 💪
