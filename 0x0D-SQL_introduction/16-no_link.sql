-- Lists all records of a table second_table with names in descending order.
-- Lists all records of a table second_table with names in descending order.
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
