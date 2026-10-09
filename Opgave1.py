#opgave 1 Et script til at definere databasens tabelstruktur – hvis I har f.eks. to tabeller så også med en
#fremmednøgle. I skal bruge CREATE TABLE-kommandoen

import sqlite3 as sql
conn = sql.connect("Gamers.db")
cur = conn.cursor()

#Creater et table og lukker
cur.execute("""CREATE TABLE Gamers(id INTEGER Primary KEY, username TEXT,First_login TEXT,Hours_played INTEGER,Last_seen_online TEXT,Main_hero TEXT)""")
conn.commit()
conn.close()



