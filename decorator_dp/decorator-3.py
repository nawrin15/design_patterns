class IceCream():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def getDescription(self) -> str:
        pass
    
    def cost(self) -> int:
        pass


class ChocolateIceCream(IceCream):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def getDescription(self) -> str:
        return "Chocolate Ice Cream"
    
    def cost(self) -> int:
        return 70

class ButterScotchIceCream(IceCream):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def getDescription(self) -> str:
        return "Butter Scotch Ice Cream"
    
    def cost(self) -> int:
        return 80

class IceCreamDecorator(IceCream):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    def getDescription(self) -> str:
        pass
    
    def cost(self) -> int:
        pass


class ChocoChipsDecorator(IceCream):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    iceCream: IceCream = None

    def __init__(self, iceCream: IceCream) -> None:
        self.iceCream = iceCream
        
    def getDescription(self) -> str:
        return f"{self.iceCream.getDescription()} with choco chips"

    def cost(self) -> str:
        return self.iceCream.cost() +30

class RainbowSprinkleDecorator(IceCream):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    iceCream: IceCream = None

    def __init__(self, iceCream: IceCream) -> None:
        self.iceCream = iceCream
        
    def getDescription(self) -> str:
        return f"{self.iceCream.getDescription()} with rainbow sprinkle"

    def cost(self) -> str:
        return self.iceCream.cost() + 20
    

class ChocoSyrupDecorator(IceCream):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    iceCream: IceCream = None

    def __init__(self, iceCream: IceCream) -> None:
        self.iceCream = iceCream
        
    def getDescription(self) -> str:
        return f"{self.iceCream.getDescription()} with choco syrup"

    def cost(self) -> str:
        return self.iceCream.cost() + 40

def client_code(iceCream: IceCream) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """
    print(f"{iceCream.getDescription()}-{iceCream.cost()}")



if __name__ == "__main__":
    base = ChocolateIceCream()
    print("Client: I've got ", end="")
    client_code(base)
    decorator1 = ChocoSyrupDecorator(base)
    print("Client: Now I've got a ", end="")
    client_code(decorator1)
    decorator2 = ChocoChipsDecorator(decorator1)
    print("Client: Now I've got a ", end="")
    client_code(decorator2)
    decorator3 = RainbowSprinkleDecorator(decorator2)
    print("Client: Now I've got a ", end="")
    client_code(decorator3)
    print("\n")