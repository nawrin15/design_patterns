from abc import ABCMeta, abstractmethod

class Pizza:
    
    def __init__(self):
        self.name = ""
        self.price = 0
        self.description = ""
        self.toppings = ""
    
    
class IPizzaBuilder(metaclass=ABCMeta):
    
    def setName(self):
        pass
    
    def setPrice(self):
        pass
    
    def setDescription(self):
        pass
    
    def setToppings(self):
        pass
    
    def getPizza(self):
        pass
    

class MargaritaBuilder(IPizzaBuilder):
    
    def __init__(self):
        self.__pizza = Pizza()
        
    def setName(self):
        self.__pizza.name = "Margarita"
        
    def setPrice(self):
        self.__pizza.price = 400
        
    def setDescription(self):
        self.__pizza.description = "Margarita medium size pizza."
        
    def setToppings(self):
        self.__pizza.toppings = ["Tomato", "Cheese"]
        
    def getPizza(self):
        return self.__pizza
    
    
class PizzaDirector:
    def build(self, builder: IPizzaBuilder):
        builder.setName()
        builder.setDescription()
        builder.setPrice()
        builder.setToppings()
        return builder.getPizza()
    
    
pizzaFactory = PizzaDirector()
selectedPizza = pizzaFactory.build(MargaritaBuilder())

print(f"You have selected {selectedPizza.name} pizza")
print(f"Description: {selectedPizza.description}")
print(f"Price: {selectedPizza.price}")
print(f"Toppings: {selectedPizza.toppings}")