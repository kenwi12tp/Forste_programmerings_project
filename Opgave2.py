#opgave 2 Et script til ”bulk-insert” af 100, 500 eller måske endnu flere data. Her må/skal I bruge en LLM til at
#generere nogle kunstige data – bed LLM’en om at give Jer f.eks. 100 INSERT INTO-statements som
#passer til Jeres datamodel


import sqlite3 as sql
import random
from datetime import datetime, timedelta
conn = sql.connect("Gamers.db")
cur = conn.cursor()

heroes = [
    "Warrior", "Mage", "Assassin", "Archer",
    "Paladin", "Necromancer", "Druid", "Berserker"
]

gamers = []

#alt data der skal i datasættet bliver skabt i dette forlob da der skal bruges 500 datasæt
for i in range(1, 501):
    username = f"Gamer{i:03d}"

    first_login = datetime.now() - timedelta(
        days=random.randint(1, 1500)
    )

    hours_played = random.randint(0, 5000)

    last_seen = datetime.now() - timedelta(
        days=random.randint(0, 30),
        hours=random.randint(0, 23)
    )

    main_hero = random.choice(heroes)

    gamers.append((
        username,
        first_login.strftime("%Y-%m-%d %H:%M:%S"),
        hours_played,
        last_seen.strftime("%Y-%m-%d %H:%M:%S"),
        main_hero
    ))

#data indsættes i databasen
cur.executemany("""
INSERT INTO Gamers
(username, First_login, Hours_played, Last_seen_online, Main_hero)
VALUES (?, ?, ?, ?, ?)
""", gamers)

conn.commit()

print("500 spillere er blevet indsat!")

conn.close()