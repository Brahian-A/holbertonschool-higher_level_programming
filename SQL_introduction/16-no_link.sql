-- script que enumera todos los registros de la tabla Second_Table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name !=''
ORDER BY score DESC;