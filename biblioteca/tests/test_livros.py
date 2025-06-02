
import os
import sys
import unittest
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, livros, next_id

class TestLivrosAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Content-Type": "application/json"}
        app.testing = True
        global livros, next_id
        livros.clear()
        next_id = 1

    def test_criar_livro(self):
        livro = {
            "titulo": "O Senhor dos Anéis",
            "autor": "J.R.R. Tolkien",
            "ano": 1954,
            "isbn": "978-8533615540"
        }
        response = self.client.post("/livros", data=json.dumps(livro), headers=self.headers)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["titulo"], livro["titulo"])

    def test_listar_livros_vazio(self):
        response = self.client.get("/livros")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 0)        

    def test_listar_livros_apos_criacao(self):
        livro = {
            "titulo": "1984",
            "autor": "George Orwell",
            "ano": 1949,
            "isbn": "978-0451524935"
        }
        self.client.post("/livros", data=json.dumps(livro), headers=self.headers)
        response = self.client.get("/livros")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertGreaterEqual(len(data), 1)
        self.assertTrue(any(l["titulo"] == "1984" for l in data))

    def test_obter_livro_existente(self):
        livro={
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "ano": 1899,
            "isbn": "978-8572329793"
        }

        post_response = self.client.post("/livros", data=json.dumps(livro),headers=self.headers)
        criado = json.loads(post_response.data)
        response = self.client.get("/livros/%d"%criado["id"])
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["titulo"], "Dom Casmurro")
        
    def test_obter_livro_inexistente(self):
        livro = {}
        response = self.client.get("/livros/9999")
        self.assertEqual(response.status_code,404)        

    def test_remover_livro_existente(self):
        livro = {
            "titulo": "Memórias Póstumas de Brás Cubas",
            "autor": "Machado de Assis",
            "ano": 1881,
            "isbn": "978-8572329794"
        }
        post_response = self.client.post("/livros", data=json.dumps(livro), headers=self.headers)
        criado = json.loads(post_response.data)
        delete_response = self.client.delete(f"/livros/{criado['id']}")
        self.assertEqual(delete_response.status_code, 204)

    def test_remover_livro_inexistente(self):
        response = self.client.delete("/livros/9999")
        self.assertEqual(response.status_code, 404)

    def test_livro_nao_encontrado_apos_remocao(self):
        livro = {
            "titulo": "Capitães da Areia",
            "autor": "Jorge Amado",
            "ano": 1937,
            "isbn": "978-8503011812"
        }
        post_response = self.client.post("/livros", data=json.dumps(livro), headers=self.headers)
        criado = json.loads(post_response.data)
        self.client.delete(f"/livros/{criado['id']}")
        get_response = self.client.get(f"/livros/{criado['id']}")
        self.assertEqual(get_response.status_code, 404)

