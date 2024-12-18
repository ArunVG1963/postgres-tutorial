import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select all records from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')
# fetch the results (multiple)
# results = cursor.fetchall()

# Query3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])


# Query4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query5

# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
# fetch the result (single)
# results = cursor.fetchone()

# Query6

cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
results = cursor.fetchall()
# close the connection
connection.close()

# print results
for result in results :
    for  x in result :
        print(x)