# import dependencies
import sqlite3
import sys

# Create the connections
conn = sqlite3.connect('Sensors.db')
curs = conn.cursor()


# Print out data from table BME_DATA
for row in curs.execute("SELECT * FROM BME_DATA ORDER BY TIME_STAMP DESC LIMIT 200"):
    print (row)

conn.close()