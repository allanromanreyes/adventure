# Futurelearn advenure game
from room import Room

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

# player location
current_room = kitchen
while True:
    print('\n')
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)


