from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Конфигурация базы данных из переменных окружения
db_config = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "rootpassword"),
    "database": os.getenv("DB_NAME", "store")
}

# Главная страница API
@app.route("/")
def home():
    return "Добро пожаловать в API интернет-магазина!"

# Эндпоинт для оформления заказа
@app.route("/api/order", methods=["POST"])
def order():
    data = request.get_json()
    name = data.get("name")
    address = data.get("address")
    if not name or not address:
        return jsonify({"error": "Необходимо указать имя и адрес"}), 400
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (name, address) VALUES (%s, %s)", (name, address))
        conn.commit()
        return jsonify({"message": "Заказ успешно создан!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)