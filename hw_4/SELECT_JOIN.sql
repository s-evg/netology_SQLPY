SELECT g.name, count(ga.artist_id) FROM genre g
   JOIN genre_artist ga ON g.id = ga.genre_id
   GROUP BY g.name;
  
SELECT al.name, al.year , count(t.id) FROM album al
   JOIN track t ON al.id = t.album_id
   WHERE al.year BETWEEN 2019 and 2020
   GROUP BY al.name, al.year;
   
SELECT al.name, AVG(t.duration) FROM album al
	JOIN track t ON al.id = t.album_id
	GROUP BY al.name;

SELECT ar.name FROM artist ar
   JOIN album_artist aa ON ar.id = aa.artist_id
   JOIN album a ON a.id = aa.album_id
   WHERE a.year < 2020; 
  
SELECT c.tille FROM collection c
   JOIN track_collection tc ON c.id = tc.collection_id
   JOIN track t ON t.id = tc.track_id
   JOIN album a ON a.id = t.album_id
   JOIN album_artist aa ON a.id = aa.album_id
   JOIN artist ar ON ar.id = aa.artist_id 
   WHERE ar.name LIKE '%ABBA%';
  
SELECT a.name FROM album a
	JOIN album_artist aa ON a.id = aa.album_id
	JOIN artist ar ON ar.id = aa.artist_id
	JOIN genre_artist ga ON ga.artist_id = ar.id
	JOIN genre g ON g.id = ga.genre_id
	GROUP BY ar.name, a.name
    HAVING count(ga.genre_id) > 1;
   
SELECT t.title FROM track t
	LEFT JOIN  track_collection tc ON t.id = tc.track_id
	WHERE tc.track_id IS null;

SELECT ar.name FROM artist ar
	JOIN album_artist aa ON ar.id = aa.artist_id 
	JOIN album a ON a.id = aa.album_id
	JOIN track t ON t.album_id = a.id
	WHERE duration = (SELECT min(duration) FROM track);

SELECT al.name , count(t.id) FROM album al
    JOIN track t ON al.id = t.album_id
    GROUP BY al.name 
    HAVING count(t.id) in (
    	SELECT count(t.id) FROM album al
    	JOIN track t ON al.id = t.album_id
        GROUP BY al.name
        ORDER BY count(t.id)
        LIMIT 1);
