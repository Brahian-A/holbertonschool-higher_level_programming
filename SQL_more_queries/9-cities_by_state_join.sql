-- Script que enumera todas las ciudades encontradas en la base de datos
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;