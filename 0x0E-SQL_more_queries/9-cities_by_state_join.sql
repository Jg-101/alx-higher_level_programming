-- lists all cities of California that can be found in db hbtn_0d_usa
SELECT cities.id, cities.name, states.name
       FROM cities
       INNER JOIN states
       ON states.id = cities.state_id
       ORDER BY cities.id;
