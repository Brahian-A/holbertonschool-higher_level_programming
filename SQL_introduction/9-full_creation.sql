-- script que crea una segunda tabla de datos y agrega varias filas

CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name VARCHAR(256),
    score int
);


-- inseta nuevas filas en la tabla 
INSERT INTO second_table (id, name, score) VALUES 
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8)
