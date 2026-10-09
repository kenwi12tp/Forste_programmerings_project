#Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet. Data skal udskrives
#pænt i konsollen.

import sqlite3 as sql
conn = sql.connect("Gamers.db")
cur = conn.cursor()

cur.execute("select * from Gamers")
data = cur.fetchall()
for row in data:
    print(f"Player:{row[1]}, Joined the at:{row[2]}, Hours played:{row[3]}, Last seen:{row[4]}, Main hero:{row[5]}")
conn.close()