from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Конфигурация базы данных из переменных окружения
db_config = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "rootpassword"),
    "database": os.getenv("DB_NAME", "store"),
    "charset": "utf8mb4"
}

# Главная страница API
@app.route("/")
def home():
    return "Добро пожаловать в API интернет-магазина!"

# Эндпоинт для оформления заказа
@app.route("/api/order", methods=["POST"])
def order():
    data = request.get_json()
    email = data.get("email")
    city = data.get("city")
    street = data.get("street")
    house = data.get("house")
    apartment = data.get("apartment", "")
    name = data.get("name")

    if not all([email, city, street, house, name]):
        return jsonify({"error": "Все обязательные поля должны быть заполнены"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (email, city, street, house, apartment, name, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (email, city, street, house, apartment, name, 'Ожидает обработки')
        )
        conn.commit()
        return jsonify({"message": "Заказ успешно создан!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Эндпоинт для проверки статуса заказа по email
@app.route("/api/order/status", methods=["GET"])
def check_order_status():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Необходимо указать email"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders WHERE email = %s", (email,))
        orders = cursor.fetchall()
        
        if not orders:
            return jsonify({"message": "Заказы не найдены"}), 404
        
        return jsonify({"orders": orders}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)