#Et script til at tilføje én ny ”record” i databasen, baseret på input fra brugeren. I skal igen bruge
#INSERT INTO-kommandoen. Det vil være super hvis der var validering af hvert enkelt felt således at
#man ikke kan komme til at indsætte en tekst under et felt som kun kan indeholde tal.

import sqlite3 as sql
conn = sql.connect("Gamers.db")
cur = conn.cursor()
from datetime import datetime
date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
heroes = [
    "Warrior", "Mage", "Assassin", "Archer",
    "Paladin", "Necromancer", "Druid", "Berserker"
]
hero_picked = False

while True:
    quit = input("\nDo you want to make a new account? (y/n)")
    if quit.lower() == "n" or quit.lower() == "no":
        break
    elif quit.lower() == "y" or quit.lower() == "yes":
        username = input("\nEnter your username: ")
        while hero_picked == False:
            hero = input(f"Heres a list of heroes pick 1\n{heroes}\nwhat hero do you wanna play ")
            hero = hero.lower()
            hero = hero.capitalize()
            if hero in heroes:
                print(f"you have chosen {hero}")
                hero_picked = True
            else:
                print(f"that's not a hero plss try again")
        while hero_picked == True:
            cur.execute("""INSERT INTO Gamers (username, First_login, Hours_played, Last_seen_online, Main_hero) VALUES (?,?,?,?,?)""",(username,date,0,date,hero))
            print(f"you have now succesfully crated your account {username}")
            conn.commit()
            hero_picked = False
    else:
        print("plss press either y or n")