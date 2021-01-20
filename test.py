import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int , username text , password text)"
cursor.execute(create_table)

user =(1, 'rahul' ,'asdf')
insert_query = " INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query ,user)

users = [
    (1, 'rahul' ,'asdf'),
    (2, 'rahu2l' ,'asd2f')
    ,(3, 'ra22hul' ,'as22df')
]
cursor.executemany(insert_query ,users)

sel = "SELECT * from users"
for row in cursor.execute(sel):
    print(row)

connection.commit()
connection.close()