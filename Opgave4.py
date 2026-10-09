#Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet. Data skal udskrives
#pænt i konsollen.

import sqlite3 as sql
conn = sql.connect("gamers.db")
cur = conn.cursor()

cur.execute("select * from Gamers")
data = cur.fetchall()
for i in data:
    print(i)