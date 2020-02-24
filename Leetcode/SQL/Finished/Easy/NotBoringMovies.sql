SELECT *
FROM cinema
HAVING description != 'boring' AND id % 2 != 0
ORDER BY rating DESC