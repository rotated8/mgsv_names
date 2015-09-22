import sqlite3, os

conn = sqlite3.connect('names.db')
c = conn.cursor()

c.execute('drop table adjectives')
c.execute('drop table animals')
c.execute('drop table rares')
c.execute('drop table uncommons')
conn.commit()

c.execute('create table adjectives (adjective text unique)')
c.execute('create table animals (animal text unique)')
c.execute('create table rares (name text unique)')
c.execute('create table uncommons (key text, value text)')
conn.commit()

with open(os.path.join(os.path.dirname(__file__), 'adjectives.txt')) as f:
    for line in f:
        c.execute('insert into adjectives values (?)', line.strip())
conn.commit()

with open(os.path.join(os.path.dirname(__file__), 'animals.txt')) as f:
    for line in f:
        c.execute('insert into animals values (?)', line.strip())
conn.commit()

with open(os.path.join(os.path.dirname(__file__), 'rares.txt')) as f:
    for line in f:
        c.execute('insert into rares values (?)', line.strip())
conn.commit()

with open(os.path.join(os.path.dirname(__file__), 'uncommons.txt')) as f:
    for line in f:
        if not line.startswith('#'):
            c.execute('insert into uncommons values (?, ?)', line.strip().split('|'))
conn.commit()

conn.close()
