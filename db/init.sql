-- Создание базы данных, если она не существует
CREATE DATABASE IF NOT EXISTS store;
USE store;

-- Создание таблицы заказов с новым полем для статуса
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,         -- Электронный адрес заказчика
    city VARCHAR(100) NOT NULL,          -- Город
    street VARCHAR(100) NOT NULL,        -- Улица
    house VARCHAR(20) NOT NULL,          -- Номер дома
    apartment VARCHAR(20),               -- Номер квартиры (может быть NULL)
    name VARCHAR(255) NOT NULL,          -- Имя заказчика
    status VARCHAR(50) DEFAULT 'Ожидает обработки' -- Статус заказа (по умолчанию 'Ожидает обработки')
);