import pymysql
import os

import dotenv

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS artist ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'name VARCHAR(300) NOT NULL,'
            'PRIMARY KEY (id)'
            ')'
        )
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS album ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'name VARCHAR(300) NOT NULL,'
            'PRIMARY KEY (id),'
            'artist_id INT NOT NULL,'
            'FOREIGN KEY (artist_id) REFERENCES artist(id)'
            ')'
        )
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS genre ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'name VARCHAR(50) NOT NULL,'
            'PRIMARY KEY (id)'
            ')'
        )
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS song ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'artist_id INT NOT NULL,'
            'album_id INT NOT NULL,'
            'genre_id INT NOT NULL,'
            'name VARCHAR(300) NOT NULL,'
            'PRIMARY KEY (id),'
            'FOREIGN KEY (artist_id) REFERENCES artist(id),'
            'FOREIGN KEY (album_id) REFERENCES album(id),'
            'FOREIGN KEY (genre_id) REFERENCES genre(id)'
            ')'
        )
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(
            'INSERT INTO artist (name) VALUES '
            '("The Beatles"), '
            '("Pink Floyd"), '
            '("Taylor Swift"), '
            '("ABBA"), '
            '("Iron Maiden")'
        )
        cursor.execute(
            'INSERT INTO album (name, artist_id) VALUES '
            '("Abbey Road", (SELECT id FROM artist WHERE name = "The Beatles")), '
            '("Revolver", (SELECT id FROM artist WHERE name = "The Beatles")), '
            '("The Dark Side Of The Moon", (SELECT id FROM artist WHERE name = "Pink Floyd")), '
            '("The Wall", (SELECT id FROM artist WHERE name = "Pink Floyd")), '
            '("1989", (SELECT id FROM artist WHERE name = "Taylor Swift")), '
            '("Arrival", (SELECT id FROM artist WHERE name = "ABBA")), '
            '("The Number Of The Beast", (SELECT id FROM artist WHERE name = "Iron Maiden"))'
        )
        cursor.execute(
            'INSERT INTO genre (name) VALUES '
            '("Rock"), '
            '("Heavy Metal"), '
            '("Pop")'
        )
        cursor.execute(
            'INSERT INTO song (name, artist_id, album_id, genre_id) VALUES '
            '("Come Together" ,'
            '(SELECT id FROM artist WHERE name = "The Beatles"), '
            '(SELECT id FROM album WHERE name = "Abbey Road"), '
            '(SELECT id FROM genre WHERE name = "Rock")'
            '), '

            '("Something", '
            '(SELECT id FROM artist WHERE name = "The Beatles"), '
            '(SELECT id FROM album WHERE name = "Abbey Road"), '
            '(SELECT id FROM genre WHERE name = "Rock")'
            '), '

            '("Yellow Submarine", '
            '(SELECT id FROM artist WHERE name = "The Beatles"), '
            '(SELECT id FROM album WHERE name = "Revolver"), '
            '(SELECT id FROM genre WHERE name = "Rock")'
            '), '

            '("Money", '
            '(SELECT id FROM artist WHERE name = "Pink Floyd"), '
            '(SELECT id FROM album WHERE name = "The Dark Side Of The Moon"), '
            '(SELECT id FROM genre WHERE name = "Rock")'
            '), '

            '("Another Brick In The Wall (Part 2)", '
            '(SELECT id FROM artist WHERE name = "Pink Floyd"), '
            '(SELECT id FROM album WHERE name = "The Wall"), '
            '(SELECT id FROM genre WHERE name = "Rock")'
            '), '

            '("Comfortably Numb", '
            '(SELECT id FROM artist WHERE name = "Pink Floyd"), '
            '(SELECT id FROM album WHERE name = "The Wall"), '
            '(SELECT id FROM genre WHERE name = "Rock")'
            '), '

            '("Shake It Out" ,'
            '(SELECT id FROM artist WHERE name = "Taylor Swift"), '
            '(SELECT id FROM album WHERE name = "1989"), '
            '(SELECT id FROM genre WHERE name = "Pop")'
            '), '

            '("Style" ,'
            '(SELECT id FROM artist WHERE name = "Taylor Swift"), '
            '(SELECT id FROM album WHERE name = "1989"), '
            '(SELECT id FROM genre WHERE name = "Pop")'
            '), '

            '("Dancing Queen" ,'
            '(SELECT id FROM artist WHERE name = "ABBA"), '
            '(SELECT id FROM album WHERE name = "Arrival"), '
            '(SELECT id FROM genre WHERE name = "Pop")'
            '), '

            '("The Number Of The Beast" ,'
            '(SELECT id FROM artist WHERE name = "Iron Maiden"), '
            '(SELECT id FROM album WHERE name = "The Number Of The Beast"), '
            '(SELECT id FROM genre WHERE name = "Heavy Metal")'
            '), '

            '("Run To The Hills" ,'
            '(SELECT id FROM artist WHERE name = "Iron Maiden"), '
            '(SELECT id FROM album WHERE name = "The Number Of The Beast"), '
            '(SELECT id FROM genre WHERE name = "Heavy Metal")'
            ')'
        )

        connection.commit()
