#Et script til at filtrere data (lave en udvælgelse med SELECT). Det kunne f.eks. være alle students der
#bor i Esbjerg.

import sqlite3 as sql
conn = sql.connect("Gamers.db")
cur = conn.cursor()

cur.execute("SELECT * FROM Gamers WHERE Hours_played > 3000")
data = cur.fetchall()

print("Here is all our Champions")
for row in data:
    print(f"player:{row[1]} has {row[3]} Hours played and is therefor a champion")
conn.close()

