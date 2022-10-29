CREATE TABLE IF NOT EXISTS genre (
id serial PRIMARY KEY, 
name varchar(100) NOT NULL UNIQUE);

CREATE TABLE IF NOT EXISTS artist (
id serial PRIMARY KEY, 
name varchar(100) NOT NULL UNIQUE, 
nick varchar(100) UNIQUE);
	
CREATE TABLE IF NOT EXISTS genre_artist (
genre_id integer REFERENCES genre(id), 
artist_id integer REFERENCES artist(id), 
CONSTRAINT genre_artist_pk PRIMARY KEY (genre_id, artist_id));	

CREATE TABLE IF NOT EXISTS album (
id serial PRIMARY KEY, 
name varchar(100) NOT NULL, 
year integer NOT NULL);
	
CREATE TABLE IF NOT EXISTS album_artist (
album_id integer REFERENCES album(id), 
artist_id integer REFERENCES artist(id), 
CONSTRAINT album_artist_pk PRIMARY KEY (album_id, artist_id));

CREATE TABLE IF NOT EXISTS track (
	id serial PRIMARY KEY, 
title varchar(100) NOT NULL, 
duration integer NOT NULL, 
album_id integer REFERENCES album(id));

CREATE TABLE IF NOT EXISTS collection (
	id serial PRIMARY KEY, 
title varchar(100) NOT NULL, 
year integer NOT NULL);

CREATE TABLE IF NOT EXISTS track_collection (
track_id integer REFERENCES track(id), 
collection_id integer REFERENCES collection(id), 
CONSTRAINT track_collection_pk PRIMARY KEY (track_id, collection_id));