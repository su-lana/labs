import sqlite3

con = sqlite3.connect('lab3.db')
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute('''CREATE TABLE IF NOT EXISTS BLOCKS (
            id TEXT PRIMARY KEY,
            view INTEGER,
            desc TEXT,
            img BLOB
            )
''')
cur.execute('''CREATE TABLE IF NOT EXISTS SOURCES (
            id INTEGER PRIMARY KEY,
            ip_addr TEXT,
            country_code TEXT
            )
''')
cur.execute('''CREATE TABLE IF NOT EXISTS PERSONS (
            id INTEGER PRIMARY KEY,
            name TEXT,
            addr TEXT
            )
''')
cur.execute('''CREATE TABLE IF NOT EXISTS VOTES (
            block_id TEXT,
            voter_id INTEGER,
            timestamp DATETIME,
            source_id INTEGER,
            PRIMARY KEY (block_id, voter_id),
            FOREIGN KEY (block_id) REFERENCES BLOCKS(id),
            FOREIGN KEY (voter_id) REFERENCES PERSONS(id),
            FOREIGN KEY (source_id) REFERENCES SOURCES(id)
            )
''')

cur.execute("INSERT INTO BLOCKS VALUES ('0x123', 0, 'what am i supposed to write here', NULL)")
cur.execute("INSERT INTO PERSONS VALUES (0, 'John', 'Lviv')")
cur.execute("INSERT INTO SOURCES VALUES (1, '195.211.85.187', 'UA')")
cur.execute("INSERT INTO VOTES VALUES ('0x123', 0, '2025-03-03 12:00:00', 1)")

con.commit()
con.close()