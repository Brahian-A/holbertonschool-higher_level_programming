-- Crea una base de batos si ya no existe
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Usa la nueva base de batos 
USE hbtn_0d_usa;

-- Crea una tabla si ya no existe
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);
