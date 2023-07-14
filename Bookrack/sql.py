# import sqlite3            # 'tworzenie tabeli z książkami'
#
# conn = sqlite3.connect('my_library.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS books')
# cur.execute('CREATE TABLE books (title TEXT, author TEXT, category TEXT, status TEXT, comment TEXT)')
#
# conn.close()

# import sqlite3            # 'dodawanie książek'
#
# conn = sqlite3.connect('my_library.sqlite')
# cur = conn.cursor()
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Chemia Śmierci', 'Simon Beckett', 'kryminał', 'przeczytana', 'Dr.Hunter'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Zapisane w kościach', 'Simon Beckett', 'kryminał', 'przeczytana', 'Dr.Hunter'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Szepty zmarłych', 'Simon Beckett', 'kryminał', 'przeczytana', 'Dr.Hunter'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Wołanie grobu', 'Simon Beckett', 'kryminał', 'przeczytana', 'Dr.Hunter'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Zabij mnie znów', 'Rachel Abbott', 'kryminał', 'przeczytana', 'Tom Douglas'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Zabij mnie znów', 'Rachel Abbott', 'kryminał', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('7 EW', 'Neal Stephenson', 'sci-fi', 'nieprzeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Cari Mora', 'Thomas Harris', 'kryminał', 'nieprzeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Chirurg', 'Tess Gerritsen', 'kryminał', 'przeczytana', 'anatomia zbrodni'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Dawca', 'Tess Gerritsen', 'kryminał', 'przeczytana', 'anatomia zbrodni'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Dotyk zła', 'Alex Kava', 'kryminał', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ("Droga Steve'a Jobsa", 'Brent Schlender', 'biograficzna', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Dwadzieścia tysięcy mil podmorskiej żeglugi', 'Jules Verne', 'sci-fi', 'przeczytana', 'Nemo'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Hyperion', 'Dan Simmons', 'sci-fi', 'przeczytana', 'Hyperion'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Zagłada Hyperiona', 'Dan Simmons', 'sci-fi', 'przeczytana', 'Hyperion'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Idealny stan', 'Brandon Sanderson', 'sci-fi', 'przeczytana', 'krótkie opowiadanie'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Kolor Magii', 'Terry Pratchett', 'fantasy', 'przeczytana', 'świat dysku'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Krucyfiks', 'Chris Carter', 'kryminał', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Łzy Mai', 'Martyna Raduchowska', 'sci-fi', 'przeczytana', 'czarne światła'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Spektrum', 'Martyna Raduchowska', 'sci-fi', 'przeczytana', 'czarne światła'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Metro 2034', 'Dmitry Glukhovsky', 'sci-fi', 'przeczytana', 'metro'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Metro 2035', 'Dmitry Glukhovsky', 'sci-fi', 'przeczytana', 'metro'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Niezwycięzony', 'Stanislaw Lem', 'sci-fi', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Obce dziecko', 'Rachel Abbott', 'kryminał', 'przeczytana', 'Tom Douglas'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Pasażer 23', 'Sebastian Fitzk', 'kryminał', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Profil mordercy', 'Paul Britton', 'kryminał', 'w trakcie'))
#
# cur.execute('INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)',
#     ('Rok 1984', 'George Orwell', 'kryminał', 'przeczytana'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Śpij spokojnie', 'Rachel Abbott', 'kryminał', 'przeczytana', 'Tom Douglas'))
#
# cur.execute('INSERT INTO books (title, author, category, status, comment) VALUES (?, ?, ?, ?, ?)',
#     ('Szóste okno', 'Rachel Abbott', 'kryminał', 'przeczytana', 'Tom Douglas'))
#
# conn.commit()
#
# cur.close()

#
# import sqlite3  # 'wyświetlanie tabeli'
#
# conn = sqlite3.connect('my_library.sqlite')
# cur = conn.cursor()
#
# cur.execute('SELECT title, author, category, status, comment FROM books')
# for row in cur:
#     print(row)
#
# conn.close()

