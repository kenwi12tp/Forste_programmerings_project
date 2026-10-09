#Opgave3 Et script til at tømme tabellerne for data. Her bruges DELETE FROM kommandoen.
import sqlite3 as sql
conn = sql.connect("Gamers.db")
cur = conn.cursor()

cur.execute("DELETE FROM Gamers")
conn.commit()
conn.close()
