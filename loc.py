import random
from speaker import Speaker

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def add_connection(self, direction, location):
        self.connections[direction] = location

    def get_connections(self):
        return self.connections.keys()

class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
        self.inventory = []

    def move(self, direction):
        if direction in self.current_location.get_connections():
            self.current_location = self.current_location.connections[direction]
            a = "You move to "+self.current_location.name
            print("You move to", self.current_location.name)
            Speaker.speak(a)
            print(self.current_location.description)
            b = self.current_location.description
            Speaker.speak(b)
        else:
            print("You cannot go in that direction.")
            Speaker.speak("You cannot go in that direction.")

    def take_item(self, item):
        self.inventory.append(item)
        a = "You pick up the "+item
        print("You pick up the", item)
        Speaker.speak(a)

    def use_item(self, item):
        if item in self.inventory:
            a = "You cannot use the "+item
            print("You cannot use the", item)
            Speaker.speak(a)
        else:
            a = "You don't have the "+item
            print("You don't have the", item)
            Speaker.speak(a)
