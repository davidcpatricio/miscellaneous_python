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
