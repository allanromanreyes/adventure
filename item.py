# Futurelearn adventure game
# Item Class

class Item():
    def __init__(self, item_name): # add a constructor
        self.name = item_name
        self.description = None
        self.linked_rooms = {}
                
    def set_description(self, item_description):
        self.description = item_description
        
    def get_description(self):
        return self.descrption
        
    def set_name(self):
        self.name = item_name
        
    def get_name(self):
        return self.name
    
    def describe(self):
        print( self.description )