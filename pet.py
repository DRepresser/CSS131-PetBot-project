import random
from datetime import datetime


class Pet:
    def __init__(self, name, species, owner_id):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.mood = 50
        self.age = None
        self.birthdate = datetime.now()
        self.lastupdate = datetime.now()
        self.owner_id = owner_id

    def feed(self, item):
        self.hunger += item.hunger
        if self.hunger >= 100:
            self.hunger = 100
        self.energy += item.energy
        if self.energy >= 100:
            self.energy = 100
        self.mood += item.mood
        if self.mood >= 100:
            self.mood = 100

    def update(self):
        time = (datetime.now() - self.lastupdate).total_seconds()/60
        self.age = datetime.now().day - self.birthdate.day
        if time >= 1:
            decrease_hunger = 0.1 * time
            decrease_energy = 0.15 * time
            decrease_mood = 0.2 * time

            increase_energy = 0.1 * time
            increase_mood = 0.2 * time

            self.hunger -= decrease_hunger
            if self.hunger <= 0:
                self.hunger = 0
            if self.hunger <= 90:
                self.energy -= decrease_energy
                if self.energy <= 0:
                    self.energy = 0
            else:
                self.energy += increase_energy
                if self.energy >= 100:
                    self.energy = 100
            if self.energy <= 90:
                self.mood -= decrease_mood
                if self.energy <= 0:
                    self.energy = 0
            else:
                self.mood += increase_mood
                if self.mood >= 100:
                    self.mood = 100
            self.lastupdate = datetime.now()
