import unittest
from app import app

class TestEstoqueAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_criar_e_listar_produto(self):
        resposta = self.client.post("/produtos", json={
            "nome": "Arroz",
            "categoria": "Alimentos",
            "quantidade_inicial": 10,
            "preco_unitario": 5.5
        })
        self.assertEqual(resposta.status_code, 201)
        dados = resposta.get_json()
        self.assertEqual(dados["nome"], "Arroz")

        resposta = self.client.get("/produtos")
        self.assertEqual(resposta.status_code, 200)
        self.assertGreaterEqual(len(resposta.get_json()), 1)

    def test_saida_estoque_invalida(self):
        self.client.post("/produtos", json={
            "nome": "Feijão",
            "categoria": "Alimentos",
            "quantidade_inicial": 2,
            "preco_unitario": 7.0
        })
        resposta = self.client.post("/produtos/2/saida", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 400)

    def test_entrada_estoque(self):
        resposta = self.client.post("/produtos/1/entrada", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["quantidade"], 15)

if __name__ == '__main__':
    unittest.main()
