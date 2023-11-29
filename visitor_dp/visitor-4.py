from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, book):
        pass
    @abstractmethod
    def visit(self, medicine):
        pass

class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Visitable):
    def __init__(self, price):
        self.price = price
    def accept(self, visitor):
        return visitor.visit(self)

    def getPrice(self):
        return self.price

class Medicine(Visitable):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit(self)

    def getPrice(self):
        return self.price

class LiteracyMissionVisitor(Visitor):
    def __init__(self, percentagediscountOnBook):
        self.discount = percentagediscountOnBook
    def visit(self, book):
        book.price = book.price - (book.price * self.discount)/100
        return book.price

class HealthMissionVisitor(Visitor):
    def __init__(self, percentagediscountOnMedicine):
        self.discount = percentagediscountOnMedicine

    def visit(self, medicine):
        medicine.price = medicine.price - (medicine.price * self.discount)/100
        return medicine.price




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    literacyMissionVisitor = LiteracyMissionVisitor(50)

    chandaMama = Book(100)

    print("Original price of the book is ", chandaMama.getPrice())

    print("Due to literacy mission, there is huge discount on the book. \
        After discount, the price is ", chandaMama.accept(literacyMissionVisitor))

    healthDriveVisitor = HealthMissionVisitor(70)

    vitaminDCapsule = Medicine(200)

    print("Original price of the medinine is ", vitaminDCapsule.getPrice())

    print("Due to health  mission the reduced price of the \
            medicine is ", vitaminDCapsule.accept(healthDriveVisitor))