import sqlite3

with sqlite3.connect("sample_sqlite3.db") as connection:
    c = connection.cursor()
    # """ and ' is the same function
    c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
    c.execute('INSERT INTO posts VALUES("Good","I am good.")')
    c.execute('INSERT INTO posts VALUES("Better","I am even better.")')

'''
run sqlite com from bash shell
sqlite> .exit
(flask_venv) Eddys-MBP:2_proj eddy$ sqlite3 sample_sqlite3_db 
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> select * from posts;
Good|I am good.
Better|I am even better.
sqlite> 
'''

'''
this is an old way to create db from SQL command
this is replaced with SQLAlchemy 
'''