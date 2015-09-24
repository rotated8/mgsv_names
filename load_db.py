from __future__ import unicode_literals, print_function
import sqlite3, os

def insert(cursor, table, line):
    if not line.startswith('#'):
        values = line.strip().split(',')
        n_values = ', '.join(('?' for _ in values))
        try:
            cursor.execute('insert into {} values ({});'.format(table, n_values), values)
        except sqlite3.OperationalError as error:
            print('Skipped `{}`, it was rejected by the database:\n{}'.format(line, error))

if __name__ == '__main__':
    schema = {
            # Table_name: row_definitions
            'adjectives': 'adjective text unique',
            'animals': 'animal text unique',
            'rares': 'name text unique',
            'uncommons': 'key text, value text',
    }

    connection = sqlite3.connect('names.db')
    cursor = connection.cursor()

    for table, columns in schema.items():
        cursor.execute('drop table {};'.format(table))
        cursor.execute('create table {} ({});'.format(table, columns))
        connection.commit()

        with open(os.path.join(os.path.dirname(__file__), table + '.txt')) as f:
            for line in f:
                insert(cursor, table, line)
        connection.commit()

    connection.close()
