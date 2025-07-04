-- script que enumera el número de registros con la misma puntuación en la tabla Second_table 
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
