 INSERT INTO geners(gener_name)
 VALUES
('Rap'),
('POP'),
('Classic'),
('Jazz'),
('Reggae'),
('Folk');

 INSERT INTO performers(performer_name)
 VALUES 
('Кипелов'),
('Децл'),
('Жуков'),
('Басков'),
('Морген'),
('Армстронг'),
('Марли'),
('Зыкина');

 INSERT INTO generperformer(performer_id, gener_id)
 VALUES 
(1, 6),
(2, 1),
(3, 2),
(4, 3),
(5, 1),
(6, 4),
(7, 5),
(8, 6),
(1, 2);

INSERT INTO albums(album_name, album_year)
 VALUES 
('Альбом Кипелова', 2000),
('Альбом Децла', 2022),
('Альбом Жукова', 2019),
('Альбом Баскова', 2018),
('Альбом Моргена', 2019),
('Альбом Армстронга', 2020),
('Альбом Марли', 2021),
('Альбом Зыкиной', 2022);

INSERT INTO performeralbums(performer_id, albums_id)
 VALUES 
(1, 5),
(2, 5),
(3, 6),
(4, 7),
(5, 8),
(6, 12),
(2, 10),
(8, 8),
(4, 5);

INSERT INTO tracks(track_name, duration, albums_id)
 VALUES 
('Мой Кипелов', 231, 5),
('Мой Децл', 209, 6),
('Мой Жуков', 210, 7),
('Не мой Басков', 211, 8),
('МойМой', 600, 9),
('Wat a Wonderful World', 36, 10),
('Sun is shining', 512, 11),
('Trach183', 999, 12),
('Track', 123, 5),
('Track128', 200, NUll),
('Track128', 200, NULL),
('Алешка', 180, 7),
('Роза', 250, 8),
('Panch', 300, 9),
('WTF', 99, 10);

INSERT INTO collections(coll_name, coll_year)
 VALUES 
('Коллекция Кипелов', 2000),
('Коллекция Децл', 2005),
('Коллекция Жуков', 2018),
('Коллекция Басков', 2020),
('Коллекция остальное', 2019),
('Прочее', 2023),
('Закат', 2019),
('Коллекция Осень', 2019),
('Прочее', 2023),
('Закат', 2019);

INSERT INTO trackcollection(track_id, collection_id)
 VALUES 
(9, 1),
(10, 2),
(11, 3),
(12, 4),
(13, 5),
(14, 5),
(15, 5);