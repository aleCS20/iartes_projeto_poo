
from flask import Flask, jsonify, request

app = Flask(__name__)
livros = []
next_id = 1

@app.route("/livros", methods=["POST"])
def criar_livro():
    global next_id
    dados = request.get_json()
    livro = {"id": next_id, **dados}
    livros.append(livro)
    next_id += 1
    return jsonify(livro), 201

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros), 200

@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro), 200
    return jsonify({}), 404

@app.route("/livros/<int:id>", methods=["DELETE"])
def remover_livro(id):
    global livros
    for livro in livros:
        if livro['id'] == id:
            livros = [l for l in livros if l['id'] != id]
            return '', 204
    return jsonify({"erro": "Livro não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
