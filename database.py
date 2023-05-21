import random
import sqlite3
from datetime import datetime
from pet import Pet
from player import Player
from item import Item


def create_table():
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS players
                (id INTEGER PRIMARY KEY,
                name TEXT,
                credits INTEGER)
                ''')
    c.execute('''CREATE TABLE IF NOT EXISTS pets
                (name TEXT,
                species TEXT,
                hunger INTEGER,
                energy INTEGER,
                mood INTEGER,
                age INTEGER,
                birthdate TEXT,
                lastupdate TEXT,
                owner_id INTEGER)
                ''')
    c.execute('''CREATE TABLE IF NOT EXISTS items
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                cost INTEGER,
                hunger INTEGER,
                energy INTEGER,
                mood INTEGER,
                file TEXT)
                ''')
    conn.commit()
    conn.close()


def insert_player(id, name):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO players VALUES (?, ?, ?)", (id, name, 100))
    conn.commit()
    conn.close()


def get_player(id):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM players WHERE id=?", (id,))
    player_data = c.fetchone()
    conn.close()
    if player_data is None:
        return None
    return Player(*player_data)


def update_player_credits(id, credits):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("UPDATE players SET credits=? WHERE id=?", (credits, id))
    conn.commit()
    conn.close()


def insert_pet(pet):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO pets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (pet.name, pet.species, pet.hunger, pet.energy, pet.mood,
               pet.age, pet.birthdate, pet.lastupdate, pet.owner_id))
    conn.commit()
    conn.close()
    return


def get_pet(owner_id):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pets WHERE owner_id=?", (owner_id,))
    pet_data = c.fetchone()
    conn.close()
    if pet_data is None:
        return None
    pet = Pet(pet_data[0], pet_data[1], pet_data[8])
    pet.hunger = pet_data[2]
    pet.energy = pet_data[3]
    pet.mood = pet_data[4]
    pet.age = pet_data[5]
    pet.birthdate = datetime.strptime(pet_data[6], '%Y-%m-%d %H:%M:%S.%f')
    pet.lastupdate = datetime.strptime(pet_data[7], '%Y-%m-%d %H:%M:%S.%f')
    return pet


def update_pet(pet):
    pet.update()
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("UPDATE pets SET hunger=?, energy=?, mood=?, age=?, lastupdate=?, owner_id=? WHERE name=?",
              (pet.hunger, pet.energy, pet.mood,
               pet.age, pet.lastupdate, pet.owner_id, pet.name))
    conn.commit()
    conn.close()

def insert_item(item):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO items (name, cost, hunger, energy, mood, file, fname) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"
              .format(item.name, item.cost, item.hunger, item.energy, item.mood, item.file, item.fname))
    conn.commit()
    conn.close()


def random_shop():
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("SELECT Max(id) FROM items")
    max_id = c.fetchone()
    random_item = []
    random_list = set()
    while len(random_list) < 5:
        random_list.add(random.randint(1, max_id[0]+1))
    for j in random_list:
        item = get_item(j)
        random_item.append(item)
    return random_item


def get_item(id):
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE id=?", (id,))
    item_data = c.fetchone()
    conn.close()
    item = Item(item_data[1], item_data[2], item_data[3], item_data[4], item_data[5], item_data[6])
    return item

