import sqlite3
import pandas as pd

class Item:
    def __init__(self, name, cost, hunger, energy, mood, file):
        self.name = name
        self.cost = cost
        self.hunger = hunger
        self.energy = energy
        self.mood = mood
        self.file = file

def load_item():
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    data = pd.read_csv('fruit_list.csv')
    df = pd.DataFrame(data)
    for row in df.itertuples():
        c.execute("INSERT INTO items (name, cost, hunger, energy, mood, file) VALUES (?, ?, ?, ?, ?, ?)",
                  (row.name, row.cost, row.hunger, row.energy, row.mood, row.file))
    conn.commit()

