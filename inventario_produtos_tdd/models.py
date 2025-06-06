# arquivo models responsável por toda a lógica do négocio do app
estoque = []
proximo_id = 1

# classe produto que representa o estoque da empresa
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

    # Retorna um dicionário com os dados do produto para ser usado como json
    def to_dict(self):
        return self.__dict__

# Cria um novo produto com e adiciona os dados ao estoque.
def criar_produto(dados):
    produto = Produto(
        nome=dados["nome"],
        categoria=dados["categoria"],
        quantidade=dados["quantidade_inicial"],
        preco=dados["preco_unitario"]
    )
    estoque.append(produto)
    
    return produto.to_dict()

# Retorna uma lista de produtos de acordo com os filtros repassados
def listar_produtos(filtro_nome=None, filtro_categoria=None):
    produtos_filtrados = estoque

    # aplicando os filtros --> nome ou categoria
    if filtro_nome:
        nome_filtrado = filtro_nome.lower()
        produtos_filtrados = [
            p for p in produtos_filtrados
            if nome_filtrado in p.nome.lower()
        ]
    if filtro_categoria:
        categoria_filtrada = filtro_categoria.lower()
        produtos_filtrados = [
            p for p in produtos_filtrados
            if categoria_filtrada in p.categoria.lower()
        ]

    return [produto.to_dict() for produto in produtos_filtrados]

# Retorna um produto conforme o ID informado e caso não encontre exibirá --> none.
def obter_produto_por_id(pid):
    for p in estoque:
        if p.id == pid:
            return p
        
    return None

# Atualiza os dados de um produto existente com base no ID informado
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

# Remove um produto do estoque com base no ID informado
def remover_produto(pid):
    global estoque

    estoque = [
        produto for produto in estoque
        if produto.id != pid
    ]

# Registra entrada de produtos no estoque e aumenta a quantidade de um produto existente.
def entrada_estoque(pid, qtd):
    if qtd <= 0:
        return None
    produto = obter_produto_por_id(pid)
    if produto:
        produto.quantidade += qtd
        return produto.to_dict()
    
    return None

# Registra saída de produtos do estoque e diminui a quantidade, caso extiste o suficiente.
def saida_estoque(pid, qtd):
    if qtd <= 0:
        return None
    produto = obter_produto_por_id(pid)
    if produto and produto.quantidade >= qtd:
        produto.quantidade -= qtd
        return produto.to_dict()
    
    return None

