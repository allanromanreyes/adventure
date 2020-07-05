# Futurelearn - adventure game

class Room():
    def __init__(self, room_name): # add a constructor
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        
    def set_description(self, room_description):
        self.description = room_description
    def get_description(self):
        return self.descrption
        
    def set_name(self):
        self.name = room_name
    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character
    def get_character(self):
        return self.character
    
    def describe(self):
        print( self.description )
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print( self.name + " linked rooms :" + repr(self.linked_rooms) )
        
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)
            
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way. You are likely to be eaten by a Grue.")
            return self
    
    
        