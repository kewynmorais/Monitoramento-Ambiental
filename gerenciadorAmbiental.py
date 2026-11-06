
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Servidor ambiental funcionando!"

@app.route("/api/dados", methods=["POST"])
def receber_dados():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON invalido"}), 400

    print("Dados recebidos:", dados)

    return jsonify({
        "mensagem": "Dados recebidos com sucesso"
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
