CREATE DATABASE weather_data;

USE weather_data;

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    weather_description VARCHAR(100),
    wind_speed FLOAT,
    timestamp DATETIME
);
