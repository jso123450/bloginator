import os
import sqlite3

db_filename = 'test.db'

schema_filename = 'test_schema.sql'

new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if new:
        print 'new'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'inserting data'
        
        conn.execute("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week', '2010-11-01')
        """)
        
        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2010-10-03', 'pymotw')
        """)
        
        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2010-10-10', 'pymotw')
        """)
        
        conn.execute("""
        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2010-10-17', 'pymotw')
        """)
    else:
        print 'not new'
        
conn.close()
