# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из локальной папки в контейнер
COPY . /app

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 5002 для доступа к приложению
EXPOSE 5002

# Команда для запуска приложения
CMD ["python", "delivery.py"]