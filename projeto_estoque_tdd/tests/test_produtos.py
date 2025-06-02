
import unittest
import json
from app import app

class TestAPIEstoque(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Content-Type": "application/json"}

    def test_listar_produtos_vazio(self):
        pass

    def test_criar_produto_valido(self):
        pass

    def test_operacao_saida_com_estoque_insuficiente(self):
        pass
