# arquivo de testes da API - testes dos métodos da API e a sua conformidade
import unittest
from app import app

class TestEstoqueAPI(unittest.TestCase):
    def setUp(self):
        # Cria o cliente de teste para simular requisições
        self.client = app.test_client()

    # Testa a criação e a listagem de um produto
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

    # Testa a tentativa de saída com quantidade maior que o estoque disponível
    def test_saida_estoque_invalida(self):
        self.client.post("/produtos", json={
            "nome": "Feijão",
            "categoria": "Alimentos",
            "quantidade_inicial": 2,
            "preco_unitario": 7.0
        })
        resposta = self.client.post("/produtos/2/saida", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("erro", resposta.get_json())

    # Testa a entrada de estoque de forma válida
    def test_entrada_estoque(self):
        resposta = self.client.post("/produtos/1/entrada", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["quantidade"], 15)

    # Testa o comportamento da listagem sem utilizar filtros
    def test_listar_produtos_vazio(self):
        resposta = self.client.get("/produtos")
        self.assertEqual(resposta.status_code, 200)
        lista = resposta.get_json()
        self.assertIsInstance(lista, list)
        self.assertGreaterEqual(len(lista), 0)

    # Testa saída de estoque com quantidade insuficiente
    def test_operacao_saida_com_estoque_insuficiente(self):
        # Cria um produto com estoque limitado
        self.client.post("/produtos", json={
            "nome": "Macarrão",
            "categoria": "Massas",
            "quantidade_inicial": 1,
            "preco_unitario": 3.0
        })
        # Tenta retirar mais do que o disponível no estoque de um produto
        resposta = self.client.post("/produtos/3/saida", json={"quantidade": 2})
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("erro", resposta.get_json())

if __name__ == '__main__':
    unittest.main()
