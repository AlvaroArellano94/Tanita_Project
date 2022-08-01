#CREATE DATABASE Tanita_app_db;
USE Tanita_app_db;

CREATE TABLE IF NOT EXISTS Users (
    User_id INT AUTO_INCREMENT PRIMARY KEY,
    User_name VARCHAR(100) NOT NULL,
    User_surnames VARCHAR(255),
    Gender VARCHAR(255),
    Age TINYINT NOT NULL,
    Height DECIMAL(3,2) NOT NULL,
    File_name VARCHAR(100) NOT NULL,
    CONSTRAINT CHK_GENDER CHECK (Gender="Male" or Gender="Female" or Gender="Other" or Gender="NA")
);

#drop table users;