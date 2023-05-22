from speaker import Speaker
from loc import Player, Location

class Game:
    def __init__(self):
        self.locations = {}

    def add_location(self, location):
        self.locations[location.name] = location

    def create_game(self):
        # Create locations and connections
        entrance = Location("Entrance", "You are standing at the entrance of a mysterious castle.")
        courtyard = Location("Courtyard", "You find yourself in a vast courtyard with an eerie silence.")
        garden = Location("Garden", "A beautiful garden with colorful flowers and a small pond.")
        library = Location("Library", "Rows of bookshelves line the walls in this ancient library.")
        treasure_room = Location("Treasure Room", "A room filled with treasures beyond your wildest dreams!")
        study_room = Location("Study Room", "A room full of all equipments and resources you need to become a scholar.")
        hostel = Location("Hostel", "Large and Dark Dormitories for you to spend your night and get a sound sleep for another day of work.")

        entrance.add_connection("north", courtyard)
        courtyard.add_connection("south", entrance)
        courtyard.add_connection("east", garden)
        courtyard.add_connection("west", library)
        garden.add_connection("west", courtyard)
        library.add_connection("east", courtyard)
        courtyard.add_connection("north", treasure_room)
        treasure_room.add_connection("south", courtyard)
        library.add_connection("north", study_room)
        study_room.add_connection("south", library)
        study_room.add_connection("south-east", courtyard)
        courtyard.add_connection("north-west", study_room)
        entrance.add_connection("north-east", garden)
        garden.add_connection("south-west", entrance)
        garden.add_connection("south", hostel)
        hostel.add_connection("north", garden)
        treasure_room.add_connection("east", hostel)
        hostel.add_connection("west", treasure_room)
        courtyard.add_connection("north-east", hostel)
        hostel.add_connection("south-west", courtyard)

        self.add_location(entrance)
        self.add_location(courtyard)
        self.add_location(garden)
        self.add_location(library)
        self.add_location(treasure_room)
        self.add_location(study_room)
        self.add_location(hostel)

    def start_game(self):
        self.create_game()

        name = input("Enter your name: ")
        Speaker.speak("Please enter you name")
        player = Player(name, self.locations["Entrance"])

        a = "Welcome to the Text Adventure Game, " + player.name + "!"
        print("\nWelcome to the Text Adventure Game, " + player.name + "!")
        Speaker.speak(a)
        print(player.current_location.description)
        Speaker.speak(player.current_location.description)
        b = "For any help with instructions on how to play please type in 'help'."
        print(b)
        Speaker.speak(b)

        game_over = False

        while not game_over:
            user_input = input("\nWhat do you want to do? ").lower()
            Speaker.speak("What do you want to do?")

            if user_input == "quit":
                game_over = True
                print("Thanks for playing!")
                Speaker.speak("Quitting the game.")
                Speaker.speak("Thanks for playing.")
            elif user_input.startswith("go"):
                direction = user_input.split()[1]
                player.move(direction)
            elif user_input.startswith("take"):
                item = user_input.split()[1]
                player.take_item(item)
            elif user_input.startswith("use"):
                item = user_input.split()[1]
                player.use_item(item)
            else:
                print("Invalid command. Please try again.")
                Speaker.speak("Invalid command. Please try again.")
