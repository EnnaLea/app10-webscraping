import sqlite3

# Establish a connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT band, date FROM events WHERE date='2028.10.25'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
# new_rows = [('Cats', 'Cat City', '2028.10.25'),
#             ('Dogs', 'Dog City', '2028.10.25'),
#             ('Fishes', 'Fish City', '2029.03.31') ]
# cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_rows)
# connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)


