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

## 🧪 Como testar com Insomnia (ou Postman)

Você pode usar uma ferramenta como **Insomnia** para testar a API com facilidade.

### 📁 Exemplo de JSON para criação de produto (`POST /produtos`):

```json
{
  "nome": "Café",
  "categoria": "Bebidas",
  "quantidade_inicial": 20,
  "preco_unitario": 9.5
}
```

### 📥 Entrada de estoque:

**POST** `/produtos/1/entrada`

```json
{
  "quantidade": 5
}
```

### 📤 Saída de estoque:

**POST** `/produtos/1/saida`

```json
{
  "quantidade": 3
}
```

### ✏️ Atualizar produto:

**PUT** `/produtos/1`

```json
{
  "nome": "Café Torrado",
  "preco_unitario": 10.0
}
```

### 🗑️ Deletar produto:

**DELETE** `/produtos/1`

*(sem corpo JSON)*

---

## 🗂️ Organização do Projeto

```
inventario_produtos_tdd/
├── app.py
├── routes.py
├── models.py
├── tests/
│   └── test_produtos.py
```

---