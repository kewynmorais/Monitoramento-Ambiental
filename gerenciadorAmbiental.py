
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

BANCO = "monitoramento.db"


# Inicializar o banco de dados
def inicializar_banco():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS medicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dispositivo TEXT NOT NULL,
                sensor TEXT NOT NULL,
                valor REAL NOT NULL,
                horario TEXT NOT NULL
            )
        """)


# Página inicial
@app.route("/")
def inicio():
    return "Servidor ambiental funcionando!"


# Receber medições dos ESP32
@app.route("/api/dados", methods=["POST"])
def receber_dados():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "JSON invalido"}), 400

    dispositivo = dados.get("dispositivo")
    sensor = dados.get("sensor")
    valor = dados.get("valor")

    # Validar os dados recebidos
    if (
        not isinstance(dispositivo, str)
        or not dispositivo.strip()
        or not isinstance(sensor, str)
        or not sensor.strip()
        or type(valor) not in (int, float)
    ):
        return jsonify({
            "erro": "Dados incompletos ou invalidos"
        }), 400

    # Registrar horario da medicao
    horario = datetime.now().isoformat(timespec="seconds")

    # Armazenar no SQLite
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            INSERT INTO medicoes
            (dispositivo, sensor, valor, horario)
            VALUES (?, ?, ?, ?)
        """, (dispositivo, sensor, valor, horario))

    print("Dados recebidos:", dados)

    return jsonify({
        "mensagem": "Dados recebidos com sucesso",
        "dispositivo": dispositivo,
        "sensor": sensor,
        "valor": valor,
        "horario": horario
    }), 200


# Consultar medições armazenadas
@app.route("/api/dados", methods=["GET"])
def consultar_dados():
    with sqlite3.connect(BANCO) as conexao:
        conexao.row_factory = sqlite3.Row

        registros = conexao.execute("""
            SELECT * FROM medicoes
            ORDER BY id DESC
        """).fetchall()

    medicoes = [dict(registro) for registro in registros]

    return jsonify(medicoes), 200


# Iniciar servidor
if __name__ == "__main__":
    inicializar_banco()
    app.run(host="127.0.0.1", port=5000, debug=True)
