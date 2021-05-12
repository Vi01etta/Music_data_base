import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://netology:netology1995@localhost:5432/music_site')

connection = engine.connect()


# название и год выхода альбомов, вышедших в 2018 году;
print(connection.execute("""
SELECT name, release FROM albums
WHERE release = 2018;
""").fetchall())


# название и продолжительность самого длительного трека;
print(connection.execute("""
SELECT name, duration  FROM track
ORDER BY duration DESC;
""").fetchone())

# название треков, продолжительность которых не менее 3,5 минуты;
print(connection.execute("""
SELECT name, duration  FROM track
WHERE duration >= 3.30;
""").fetchall())

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
print(connection.execute("""
SELECT name, release  FROM collections
WHERE release BETWEEN 2018 and 2020;
""").fetchall())

# исполнители, чье имя состоит из 1 слова;
print(connection.execute("""
SELECT name  FROM performer
WHERE name not LIKE '%% %%';
""").fetchall())

# название треков, которые содержат слово "мой"/"my".
print(connection.execute("""
SELECT name FROM track
WHERE name iLIKE '%%my%%';
""").fetchall())