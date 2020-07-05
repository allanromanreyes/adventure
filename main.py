# Futurelearn - advenure game

from room import Room
from character import Enemy, Character, Friend

# Kitchen
kitchen = Room("Kitchen") # instantiate Kitchen object
kitchen.set_description("A dank and dirty room buzzing with flies. There is a large swinging door to the South, complete with porthole. Looking through it, you see a well-lit dining \
room and a table that seems to be filled with foodstuffs.")

# Dining_hall
dining_hall = Room("Dining Hall") # instantiate Dining Hall object
dining_hall.set_description("A well-lit room dominated by a large dining table brimming with delectable deserts. The Kitchen is North and the Ballroom is West.")

# Ballroom
ballroom = Room("Ballroom") # instantiate Ballroom object
ballroom.set_description("This room is an old dance hall seeming to echo wih past parties from days long gone. There is a door that leads to a seemingly empty Dining Hall")

# link rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# set Enemy
dave = Enemy("Dave", "A smelly zombie") # initialize enemy
dave.describe()
dave.set_conversation("Brrlgrh... rgrhl... brains...") # set auto-response
dave.set_weakness("cheese")
dave.talk() # trigger conversation
dining_hall.set_character(dave) # place enemy

# set Friend
catrina = Friend("Catarina", "A friendly skeleton") # initialize Friend
carina.describe()
catrina.set_conversation("Why hello there...") # set auto-response
catrina.talk() # trigger conversation
ballroom.set_character(catrina) # place friend

#place charaters
from character import Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

# player location
current_room = kitchen
dead = False

while dead == False:
    print("\n")
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ")
    
    if command in ["north", "south", "east", "west"]: # check whether direction was typed
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitamt == None or isinstance(inhabitant, Enemy):
            print("There is no one here to fight with")
        else:
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                print("That's the end of the game!")
                dead = True
    elif command == "hug":
        if inhabitant == None:
            print("There is no one here to hug :(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
