#Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet. Data skal udskrives
#pænt i konsollen.

import sqlite3 as sql
conn = sql.connect("gamers.db")
cur = conn.cursor()

cur.execute("select * from Gamers")
data = cur.fetchall()
for i in data:
    print(f"Player:{i[1]}, Joined the at:{i[2]}, Hours played:{i[3]}, Last seen:{i[4]}, Main hero:{i[5]}")
conn.close()