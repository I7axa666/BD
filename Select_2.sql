SELECT gener_name, count(gener_name) AS count_performers FROM geners g
JOIN generperformer gp ON g.id = gp.gener_id 
JOIN performers p ON gp.performer_id = p.id
GROUP BY gener_name;

SELECT album_name,album_year, count(track_name) AS count_tracks FROM albums a 
JOIN tracks ON a.id = tracks.id
WHERE album_year = 2019 OR album_year = 2020
GROUP BY album_name, album_year;

SELECT album_name, AVG(duration) AS avg_duration FROM albums a 
JOIN tracks ON a.id = tracks.id 
GROUP BY album_name, duration;

SELECT performer_name, album_year FROM performers p 
JOIN performeralbums pa ON p.id = pa.performer_id
JOIN albums a ON a.id = pa.albums_id
WHERE album_year != 2020;

SELECT coll_name, performer_name FROM collections c
JOIN trackcollection tc ON tc.collection_id = c.id
JOIN tracks t ON t.id = tc.track_id
JOIN albums a ON a.id = t.albums_id
JOIN performeralbums pa ON pa.albums_id = a.id
JOIN performers p ON p.id = pa.performer_id
WHERE performer_name = 'Басков';

SELECT album_name FROM performers p 
JOIN generperformer gp ON gp.performer_id = p.id
JOIN performeralbums pa ON pa.performer_id = gp.performer_id
JOIN albums ON albums.id = pa.albums_id
GROUP BY album_name, performer_name 
HAVING count(gener_id) > 1;

SELECT track_name FROM tracks t 
LEFT JOIN trackcollection tc ON t.id = tc.track_id
WHERE track_id IS NULL;

SELECT performer_name FROM tracks t 
JOIN albums a ON a.id = t.albums_id
LEFT JOIN performeralbums pa ON pa.albums_id = a.id
LEFT JOIN performers p ON p.id = pa.performer_id
WHERE duration = (SELECT MIN(duration) FROM tracks);

SELECT album_name, COUNT(*) c FROM tracks t
LEFT JOIN albums a ON a.id = t.albums_id
GROUP BY album_name
HAVING count(*) = (SELECT min(track_count) FROM (SELECT COUNT(*) AS track_count FROM tracks t LEFT JOIN albums a ON a.id = t.albums_id GROUP BY album_name) f);
