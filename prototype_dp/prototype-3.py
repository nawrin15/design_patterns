from abc import ABC, abstractmethod
import time, datetime

# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(3)
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass  


import copy
import time

class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30

    # Overwriting Cloning Method:
    def clone(self):
        return copy.deepcopy(self)   
    
    
class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.stamina = 60
    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)
    

class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        self.mana = 100

    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self) 
    
print('Starting to create a Shopkeeper NPC: ', datetime.datetime.now().time())
shopkeeper = Shopkeeper(180, 22, 5, 8)
print('Finished creating a Shopkeeper NPC: ', datetime.datetime.now().time())
print('Attributes: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

print('Instantiating trader guild at: ', datetime.datetime.now().time())
for i in range(5):
    shopkeeper = Shopkeeper(180, 22, 5, 8)
    print(f'Finished creating a Shopkeeper NPC {i} at: ', datetime.datetime.now().time())
print('Finished instantiating trader guild at: ', datetime.datetime.now().time())


print('Instantiating trader guild at: ', datetime.datetime.now().time())
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
for i in range(5):
    shopkeeper_clone = shopkeeper_template.clone()
    print(f'Finished creating a Shopkeeper clone {i} at: ', datetime.datetime.now().time())
print('Finished instantiating trader guild at: ', datetime.datetime.now().time())


print('Instantiating 1000 NPCs: ', datetime.datetime.now().time())
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
warrior_template = Warrior(185, 22, 4, 21)
mage_template = Mage(172, 65, 8, 15)
for i in range(333):
    shopkeeper_clone = shopkeeper_template.clone()
    warrior_clone = warrior_template.clone()
    mage_clone = mage_template.clone()
    print(f'Finished creating NPC trio clone {i} at: ', datetime.datetime.now().time())
print('Finished instantiating NPC population at: ', datetime.datetime.now().time())