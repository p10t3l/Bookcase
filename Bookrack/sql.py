import sqlite3

conn = sqlite3.connect('my_library.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books')
cur.execute('CREATE TABLE books (title TEXT, author TEXT, category TEXT, status TEXT, comment TEXT)')

conn.close()



