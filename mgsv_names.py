from __future__ import unicode_literals, print_function
import sqlite3, os, random

_select = 'select {0} from {1} limit 1 offset abs(random()) % (select count({0}) from {1});'
_uncommon_select = 'select value from uncommons where key=?;'

def generate_name():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'names.db'))
    cursor = conn.cursor()

    adj = cursor.execute(_select.format('adjective', 'adjectives')).fetchone()[0]
    anim = cursor.execute(_select.format('animal', 'animals')).fetchone()[0]
    rare = cursor.execute(_select.format('name', 'rares')).fetchone()[0]
    uncommon_anim = cursor.execute(_uncommon_select, [adj]).fetchone()
    uncommon_adj = cursor.execute(_uncommon_select, [anim]).fetchone()

    conn.close()

    r = random.random()
    if r < 0.001 or r >= 0.999:
        return rare
    elif r < 0.3 and uncommon_anim is not None:
        return ' '.join((adj, uncommon_anim[0]))
    elif r >= 0.7 and uncommon_adj is not None:
        return ' '.join((uncommon_adj[0], anim))

    return ' '.join((adj, anim))

if __name__ == '__main__':
    print(generate_name())
