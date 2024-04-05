class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def display_room(self):
        print(f"\n{self.name}")
        print(self.description)
        print("Exits:", ", ".join(self.exits))

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = rooms[self.current_room.exits[direction]]
            print("You move to", self.current_room.name)
        else:
            print("You cannot go that way.")

# Define rooms
room1 = Room("Room 1", "You are in a small room with a door to the north.", {"north": 1})
room2 = Room("Room 2", "You are in a large hall with exits to the north and east.", {"north": 3, "east": 4})
room3 = Room("Room 3", "You are in a dimly lit corridor. There is an exit to the south.", {"south": 2})
room4 = Room("Room 4", "You are in a dusty library with shelves of old books. There is an exit to the west.", {"west": 2})

# Create dictionary to map room numbers to Room objects
rooms = {
    1: room1,
    2: room2,
    3: room3,
    4: room4
}

# Create player object
player = Player(room1)

# Main game loop
while True:
    player.current_room.display_room()
    command = input("What do you want to do? (Type 'north', 'east', 'south', or 'west' to move, or 'quit' to exit): ").lower()
    if command == "quit":
        print("Thanks for playing!")
        break
    elif command in ["north", "east", "south", "west"]:
        player.move(command)
    else:
        print("Invalid command. Please try again.")
