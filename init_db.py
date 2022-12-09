import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Первая публикация', 'Содержимое первой публикации')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Вторая публикация', 'Содержимое второй публикации')
            )

connection.commit()
connection.close()