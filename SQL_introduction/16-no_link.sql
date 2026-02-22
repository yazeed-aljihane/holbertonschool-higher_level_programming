-- Lists all records with a name of the table second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
