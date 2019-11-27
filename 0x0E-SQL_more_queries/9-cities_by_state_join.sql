-- Lists all cities in the hbtn_0d_usa database.
-- Lists all cities in the hbtn_0d_usa database.
SELECT cities.id, cities.name, states.name
	FROM cities, states
	WHERE cities.state_id = states.id
	ORDER BY cities.id;
