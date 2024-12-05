FROM python:3.12-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование приложения
COPY . .

# Запуск приложения
CMD ["python", "app.py"]