# arquivo de rotas para identificar os caminhos a seguir de cada requisição do app
from flask import Blueprint, jsonify, request
from models import (
    criar_produto, listar_produtos, obter_produto_por_id,
    atualizar_produto, remover_produto, entrada_estoque, saida_estoque
)

inventario_routes = Blueprint("inventario", __name__)

@inventario_routes.route("/produtos", methods=["GET"])
def rota_listar_produtos():
    nome = request.args.get("nome")
    categoria = request.args.get("categoria")
    return jsonify(listar_produtos(nome, categoria))

@inventario_routes.route("/produtos", methods=["POST"])
def rota_criar_produtos():
    dados = request.get_json()
    try:
        produto = criar_produto(dados)
        return jsonify(produto), 201
    except (KeyError, ValueError):
        return jsonify({"erro": "Dados inválidos"}), 400

@inventario_routes.route("/produtos/<int:pid>", methods=["GET"])
def rota_obter_produtos(pid):
    produto = obter_produto_por_id(pid)
    if produto:
        return jsonify(produto.to_dict())
    return jsonify({"erro": "Produto não encontrado"}), 404

@inventario_routes.route("/produtos/<int:pid>", methods=["PUT"])
def rota_atualizar_produtos(pid):
    dados = request.get_json()
    produto = atualizar_produto(pid, dados)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado ou dados inválidos"}), 404

@inventario_routes.route("/produtos/<int:pid>/entrada", methods=["POST"])
def rota_entrada_de_produtos(pid):
    dados = request.get_json()
    qtd = dados.get("quantidade", 0)
    produto = entrada_estoque(pid, qtd)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Entrada inválida"}), 400

@inventario_routes.route("/produtos/<int:pid>/saida", methods=["POST"])
def rota_saida_de_produtos(pid):
    dados = request.get_json()
    qtd = dados.get("quantidade", 0)
    produto = saida_estoque(pid, qtd)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Saída inválida ou estoque insuficiente"}), 400

@inventario_routes.route("/produtos/<int:pid>", methods=["DELETE"])
def rota_remover_produtos(pid):
    if obter_produto_por_id(pid):
        remover_produto(pid)
        return jsonify({"mensagem": "Removido"}), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

