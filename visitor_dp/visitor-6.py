from abc import ABCMeta


#################### Elements #####################
class Ifruit(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.name = None
        self.price = 0
        self.quantity = 0


        
class Apple(Ifruit):
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def accept(self, visitor):
        visitor.visit(self)

class Mango(Ifruit):
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def accept(self, visitor):
        visitor.visit(self)
    
#################### Elements #####################


#################### Visitor ######################
class IVisitor(metaclass=ABCMeta):
    def visit(self, mango:Mango):
        pass
    
    def visit(self, apple: Apple):
        pass
#################### Visitor 1######################

class DiscountVisitor(IVisitor):
    def visit(self, mango:Mango):
        print(f"Price after discount is {0.7*mango.price}")
    
    def visit(self, apple: Apple):
        print(f"Price after discount is {0.8*apple.price}")


#################### Visitor 1######################

#################### Visitor 2######################

class FruitSoldVisitor(IVisitor):
    def visit(self, mango:Mango):
        print(f"Mangos sold : {mango.quantity}")
    
    def visit(self, apple: Apple):
        print(f"Apple sold : {apple.quantity}")


#################### Visitor 2######################
#################### Visitor ######################


#################### Elements #####################

class IVisitableElement(metaclass=ABCMeta):
    def accept(visitor: IVisitor):
        pass
#################### Elements #####################


#################### Object Structure #############
class FruitStructure:
    def __init__(self, items) -> None:
        self.__fruits = items
        
    def applyVisitor(self, visitor:IVisitor):
        print("-----------Visitor details-----------")
        for fruit in self.__fruits:
            fruit.accept(visitor)
    
#################### Object Structure #############


if __name__ == "__main__":
    elements = [
        Apple(name="shimla Apple", price = 100, quantity=50),
        Mango(name="Ratnagir Mango", price = 90, quantity=60)
    ]
    fruitStructure = FruitStructure(elements)
    fruitStructure.applyVisitor(DiscountVisitor())
    fruitStructure.applyVisitor(FruitSoldVisitor())