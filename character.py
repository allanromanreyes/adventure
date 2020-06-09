# Futurelearn - adventure game

class Character():
    
    def __init__(self, char_name, char_description): # create a character
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self): # describe this character
        print( self.name + " is here!" )
        print( self.description )
        
    def set_conversation(self, conversation): # set what this character will say when talked to
        self.conversation = conversation
        
    def talk(self): # talk to this character
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
            
    def fight(self, combat_item): # fight with this character
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description) # inherits attributes and methods from Character class 
        self.weakness = None
        
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    
    def set_weakness(self, weakness): # set enemy weakness
        self.weakness = weakness
        
class Friend(Character):
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description) # inherits attributes and methods from Character class
