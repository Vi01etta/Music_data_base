import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://netology:netology1995@localhost:5432/music_site')

connection = engine.connect()

connection.execute("""INSERT INTO performer
           VALUES('The Beatles'),
           ('Eminem'),
           ('Celine Dion'),
           ('Tim McMorris'),
           ('Black Eyed Peas'),
           ('Linkin Park'),
           ('Noize MC'),
           ('Billie Eilish'),
           ('Metallica');
""")



connection.execute("""INSERT INTO genre(name)
           VALUES('Rock'),
           ('Metal'),
           ('Rap'),
           ('Rock-and-roll'),
           ('Hip-hop'),
           ('Pop'),
           ('Indie');

""")


connection.execute("""INSERT INTO albums(name, release)
           VALUES('Kamikaze', 2018),
           ('Monkey Business', 2005),
           ('Новый альбом', 2012),
           ('BE- lovely', 2019),
           ('Metallica', 1991),
           ('Protivo Gunz', 2013),
           ('Alive', 2014);

""")


connection.execute("""INSERT INTO track(albums_id, duration, name)
           VALUES(7, 3.39, 'Superhero'),
           (2, 2.15, 'Pump it'),
           (6, 2.46, 'Нету паспорта'),
           (3, 3.05, 'Вселенная бесконечна?'),
           (1, 2.49,'Greatest'),
           (5, 2.35, 'The Unforgiven'),
           (4, 3.54, 'Bad guy');
           (5, 3.15, 'Enter Sandman'),
           (1, 4.49,'The Ringer'),
           (7, 2.14, 'Life Is Beautiful');
""")

connection.execute("""INSERT INTO collections(name, release)
           VALUES('The Best So Far…', 2018),
           ('Shady XV', 2014),
           ('The Best Ballads', 2005),
           ('Chill Wind Down', 2018),
           ('Unreleased', 2011),
           ('Studio Collection', 2013),
           ('A Glimmer of Hope', 2017),
           ('iTunes Originals', 2005);

""")

connection.execute("""INSERT INTO collectionstrack
           VALUES(7, 1),
           (3, 6),
           (5, 3),
           (5, 4),
           (2, 5),
           (2, 2);
""")

connection.execute("""INSERT INTO genreperformer
           VALUES(1, 1),
           (1, 6),
           (2, 9),
           (3, 7),
           (3, 6),
           (3, 2),
           (4, 1),
           (5, 4),
           (5, 5),
           (5, 7),
           (5, 2),
           (6, 8),
           (6, 5),
           (6, 3),
           (7, 4),
           (7, 8);
""")


connection.execute("""INSERT INTO performeralbums
           VALUES(7, 4),
           (2, 5),
           (3, 7),
           (6, 7),
           (4, 8),
           (5, 9),
           (1, 2);
""")