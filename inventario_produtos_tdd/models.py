estoque = []
proximo_id = 1

class Produto:
    def __init__(self, nome, categoria, quantidade, preco):
        if quantidade < 0 or preco <= 0:
            raise ValueError("Quantidade deve ser >= 0 e preço > 0")
        global proximo_id
        self.id = proximo_id
        proximo_id += 1
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco_unitario = preco

    def to_dict(self):
        return self.__dict__

def criar_produto(dados):
    produto = Produto(
        nome=dados["nome"],
        categoria=dados["categoria"],
        quantidade=dados["quantidade_inicial"],
        preco=dados["preco_unitario"]
    )
    estoque.append(produto)
    return produto.to_dict()

def listar_produtos(filtro_nome=None, filtro_categoria=None):
    resultado = estoque
    if filtro_nome:
        resultado = [p for p in resultado if filtro_nome.lower() in p.nome.lower()]
    if filtro_categoria:
        resultado = [p for p in resultado if filtro_categoria.lower() in p.categoria.lower()]
    return [p.to_dict() for p in resultado]

def obter_produto_por_id(pid):
    for p in estoque:
        if p.id == pid:
            return p
    return None

def atualizar_produto(pid, dados):
    produto = obter_produto_por_id(pid)
    if not produto:
        return None
    if "nome" in dados:
        produto.nome = dados["nome"]
    if "categoria" in dados:
        produto.categoria = dados["categoria"]
    if "preco_unitario" in dados and dados["preco_unitario"] > 0:
        produto.preco_unitario = dados["preco_unitario"]
    return produto.to_dict()

def remover_produto(pid):
    global estoque
    estoque = [p for p in estoque if p.id != pid]

def entrada_estoque(pid, qtd):
    if qtd <= 0:
        return None
    produto = obter_produto_por_id(pid)
    if produto:
        produto.quantidade += qtd
        return produto.to_dict()
    return None

def saida_estoque(pid, qtd):
    if qtd <= 0:
        return None
    produto = obter_produto_por_id(pid)
    if produto and produto.quantidade >= qtd:
        produto.quantidade -= qtd
        return produto.to_dict()
    return None
