from flask import Flask, jsonify, request

# Создание Flask-приложения
app = Flask(__name__)

# Примерная логика для расчёта стоимости доставки
@app.route('/api/delivery', methods=['POST'])
def calculate_delivery():
    # Получаем данные от пользователя (например, расстояние и вес)
    data = request.get_json()
    
    if 'distance' not in data or 'weight' not in data:
        return jsonify({"error": "Не указаны все необходимые данные (расстояние и вес)"}), 400
    
    distance = data['distance']  # расстояние в километрах
    weight = data['weight']  # вес в килограммах
    
    # Логика для расчёта стоимости доставки
    base_cost = 100  # Базовая стоимость
    distance_cost = distance * 10  # Стоимость за километр
    weight_cost = weight * 5  # Стоимость за килограмм
    
    total_cost = base_cost + distance_cost + weight_cost

    # Возвращаем результат в формате JSON
    return jsonify({
        "total_cost": total_cost,
        "distance": distance,
        "weight": weight
    }), 200

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Приложение будет работать на порту 5002