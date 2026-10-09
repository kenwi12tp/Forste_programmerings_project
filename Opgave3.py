#Opgave3 Et script til at tømme tabellerne for data. Her bruges DELETE FROM kommandoen.
import sqlite3 as sql
conn = sql.connect("gamers.db")
cur = conn.cursor()

cur.execute("DELETE FROM Gamers")
conn.commit()
