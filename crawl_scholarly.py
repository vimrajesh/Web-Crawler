from scholarly import scholarly
import sqlite3

conn = sqlite3.connect('faculty_publications.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Publications')

cur.executescript('''
CREATE TABLE IF NOT EXISTS Faculty (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    faculty_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Publication (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    publication_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Join_Table (
    fac_id     INTEGER,
    publ_id   INTEGER,
    PRIMARY KEY (fac_id, publ_id)
);
''')

search_query = scholarly.search_author('Vinod Pathari')
author = next(search_query).fill()
# print(author.name)
cur.execute('''INSERT OR IGNORE INTO Faculty (faculty_name) VALUES ( ? )''', ( author.name, ) )
cur.execute('SELECT id FROM Faculty WHERE faculty_name = ? ', (author.name, ))
fac_id = cur.fetchone()[0]

#list of publications
pub_list= ([pub.bib['title'] for pub in author.publications])

for publ in pub_list:
    cur.execute('''INSERT OR IGNORE INTO Publication (publication_name)
        VALUES ( ? )''', ( publ, ) )
    cur.execute('SELECT id FROM Publication WHERE publication_name = ? ', (publ, ))
    publ_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Join_Table
        (fac_id, publ_id) VALUES ( ?, ? )''',
        (fac_id, publ_id) )


conn.commit()






