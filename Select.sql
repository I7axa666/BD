SELECT album_name, album_year FROM albums
WHERE album_year = 2018;

SELECT track_name, duration FROM tracks
ORDER BY duration DESC 
LIMIT 1;

SELECT track_name, duration FROM tracks
WHERE duration >= 210;

SELECT coll_name FROM collections
WHERE coll_year BETWEEN 2018 AND 2020;

SELECT performer_name FROM performers
WHERE performer_name NOT LIKE '% %';

SELECT track_name FROM tracks
WHERE lower(track_name) LIKE '%мой%' OR lower(track_name) LIKE '%my%';