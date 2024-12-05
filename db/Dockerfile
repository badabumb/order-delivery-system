# Используем официальный образ MySQL
FROM mysql:8.0

# Устанавливаем переменные окружения для MySQL
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=store

# Копируем скрипт для инициализации базы данных
COPY init.sql /docker-entrypoint-initdb.d/

# Экспортируем порт
EXPOSE 3306