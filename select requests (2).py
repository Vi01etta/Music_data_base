import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://netology:netology1995@localhost:5432/music_site')

connection = engine.connect()


# количество исполнителей в каждом жанре;
pprint(connection.execute("""
SELECT COUNT(p.name), g.name FROM performer p
JOIN genreperformer gp ON p.id = gp.performer_id
JOIN genre g ON gp.genre_id = g.id
GROUP BY g.name
""").fetchall())

# количество треков, вошедших в альбомы 2019-2020 годов;
pprint(connection.execute("""
SELECT COUNT(t.name), albums.name, albums.release FROM track t
JOIN albums ON albums.id = t.albums_id
WHERE albums.release  between 2019 and 2020
GROUP BY albums.name, albums.release
""").fetchall())


# средняя продолжительность треков по каждому альбому;
pprint(connection.execute("""
SELECT AVG(t.duration), albums.name FROM track t
JOIN albums ON albums.id = t.albums_id
GROUP BY albums.name
""").fetchall())

# все исполнители, которые не выпустили альбомы в 2020 году;
pprint(connection.execute("""
SELECT p.name, a.release FROM performer p
JOIN performeralbums pa ON p.id = pa.performer_id
JOIN albums a ON pa.album_id = a.id
WHERE NOT a.release = 2020
GROUP BY p.name, a.release
""").fetchall())


# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
pprint(connection.execute("""
SELECT c.name, p.name FROM collections c
JOIN collectionstrack ct ON c.id = ct.collections_id
JOIN track t ON ct.track_id = t.id
JOIN albums a ON t.albums_id = a.id
JOIN performeralbums pa ON pa.album_id = a.id
JOIN performer p ON pa.performer_id = p.id
WHERE p.name LIKE '%%Black Eyed Peas%%'
GROUP BY p.name, c.name
""").fetchall())

# название альбомов, в которых присутствуют исполнители более 1 жанра;
pprint(connection.execute("""
SELECT a.name, COUNT(g.name) FROM albums a
JOIN performeralbums pa ON pa.album_id = a.id
JOIN performer p ON pa.performer_id = p.id
JOIN genreperformer gp ON gp.performer_id = p.id
JOIN genre g ON gp.genre_id = g.id
GROUP BY p.name, a.name
HAVING COUNT(g.name) > 1
""").fetchall())



# наименование треков, которые не входят в сборники;
pprint(connection.execute("""
SELECT t.name, c.name FROM collections c
JOIN collectionstrack ct ON c.id = ct.collections_id
FULL OUTER JOIN track t ON ct.track_id = t.id
WHERE c.name IS NULL
GROUP BY t.name, c.name
""").fetchall())


# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
pprint(connection.execute("""
SELECT p.name, t.name FROM performer p
JOIN performeralbums pa ON pa.performer_id = p.id
JOIN albums a ON a.id = pa.album_id
JOIN track t ON a.id = t.albums_id
WHERE duration = (
    SELECT MIN(duration) FROM track);
""").fetchall())

# название альбомов, содержащих наименьшее количество треков.
pprint(connection.execute("""
SELECT a.name FROM albums a
JOIN track t ON t.albums_id = a.id
WHERE t.albums_id IN (
        SELECT albums_id FROM track
        GROUP BY albums_id
        HAVING COUNT(id) = (
                SELECT COUNT (id) FROM track
                GROUP BY albums_id
                 ORDER BY COUNT
                 LIMIT 1 )
)

order by a.name
""").fetchall())
