SELECT name, year FROM album    
	WHERE year = 2018;

SELECT title, duration FROM track    
	ORDER BY duration DESC
	LIMIT 1;
	
SELECT title FROM track 
	WHERE duration >= 210;
	
SELECT title FROM collection 
	WHERE year BETWEEN 2018 and 2020;
	
SELECT name FROM artist
	WHERE name NOT LIKE '%% %%';
	
SELECT title FROM track
	WHERE title LIKE '%%My%%';