from speaker import Speaker
from loc import Player, Location
from pygame import mixer

mixer.init()
mixer.music.load(".\\UltimateCreepy.mp3")
mixer.music.set_volume(0.8)

class Game:
    def __init__(self):
        self.locations = {}

    def add_location(self, location):
        self.locations[location.name] = location

    def create_game(self):
        # Create locations and connections
        entrance = Location("Entrance", "You are standing at the entrance of a mysterious castle. You need to cross the castle to reach your destination. But there is only one way out safely. All the best. And remember one thing. Everything here comes with a cost far more than the cost of your life.")
        courtyard = Location("Courtyard", "You find yourself in a vast courtyard with an eerie silence.")
        garden = Location("Garden", "A beautiful garden with colorful flowers and a small pond of blood which gets scarier as darkness approaches.")
        library = Location("Library", "Rows of bookshelves line the walls in this ancient library. Every book is a source of dark magic spells and techniques.")
        treasure_room = Location("Treasure Room", "A room filled with treasures beyond your wildest dreams! But remember, everything comes at a cost!!!")
        study_room = Location("Study Room", "A room full of all equipments and resources you need to become a scholar in the field of dark arts and black magic. But you have to pay for learning with a part of your soul.")
        hostel = Location("Dormitory", "Large and Dark Dormitories with an eerie silence and creepy and creaking beds for you to spend your night")
        main_castle = Location("Main Castle", "A creepy castle which once used to be the the pride of the kingdom of witches. Here every path has a cost to be paid. Be Careful on each step!!!")
        safe_exit = Location("Safe Exit","Congratulations!!! You have successfully crossed the castle and reached your destination.")
        graveyard = Location("Graveyard","You are now dead. You chose the wrong path and paid the cost with your life!!!")
        dark_arena = Location("Dark Magic Arena","Oops!!! You are now dead. A witch took away your body and soul for her black magic practice. You paid the cost of choosing the wrong path with your life.")
        limb = Location("Limb Museum","Oops!!! A witch took away your left limb to put it on the limb museum and you are now left with only one limb. You just escaped. Be careful on next step.")
        arm = Location("Arm Museum","Oops!!! A witch took away both your arms to put it on the arm museum and you are now left with no arms. You just escaped. Be careful on next step.")


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
        hostel.add_connection("north-west", main_castle)
        main_castle.add_connection("south-east", hostel)
        main_castle.add_connection("west", graveyard)
        main_castle.add_connection("nort-west", dark_arena)
        main_castle.add_connection("north", arm)
        arm.add_connection("south", main_castle)
        main_castle.add_connection("east", limb)
        limb.add_connection("west", main_castle)
        main_castle.add_connection("north-east", safe_exit)

        self.add_location(entrance)
        self.add_location(courtyard)
        self.add_location(garden)
        self.add_location(library)
        self.add_location(treasure_room)
        self.add_location(study_room)
        self.add_location(hostel)
        self.add_location(main_castle)
        self.add_location(graveyard)
        self.add_location(dark_arena)
        self.add_location(arm)
        self.add_location(limb)
        self.add_location(safe_exit)

    def start_game(self):
        self.create_game()
        mixer.music.play()

        Speaker.speak("Please enter you name")
        name = input("Enter your name: ")
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
            Speaker.speak("What do you want to do?")
            user_input = input("\nWhat do you want to do? ").lower()
            

            if user_input == "quit":
                game_over = True
                print("Thanks for playing!")
                Speaker.speak("Quitting the game.")
                Speaker.speak("Thanks for playing.")
                mixer.music.stop()
            elif user_input=="help":
                Speaker.speak("Providing you with necessary help with instructions of this Text-Based Adventure Game.")
                print("\nProviding you with necessary help with instructions of this Text-Based Adventure Game.")
                Speaker.speak("Below given are some commands and their parameters with the function they do. Kindly refer to these commands for playing this game.")
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
            
            if player.current_location.name=="Limb Museum":
                player.move("west")
            elif player.current_location.name=="Arm Museum":
                player.move("south")
            elif player.current_location.name=="Graveyard" or player.current_location.name=="Dark Magic Arena" or player.current_location.name=="Safe Exit":
                game_over = True
                print("Thanks for playing!")
                Speaker.speak("Quitting the game.")
                Speaker.speak("Thanks for playing.")
                mixer.music.stop()