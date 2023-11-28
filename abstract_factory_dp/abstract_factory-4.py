"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

from abc import ABCMeta, abstractmethod


class AbstractFactory:
    
    def createProduct1(self):
        raise NotImplementedError("createProduct1() must be defined in subclass")

    def createProduct2(self):
        raise NotImplementedError("createProduct2() must be defined in subclass")


class ConcreteFactory1(AbstractFactory):

    def createProduct1(self):
        return Product1_1()

    def createProduct2(self):
        return Product2_1()


class ConcreteFactory2(AbstractFactory):

    def createProduct1(self):
        return Product1_2()

    def createProduct2(self):
        return Product2_2()


class AbstractProduct1:

    def display(self):
        raise NotImplementedError("display() must defined in subclass")


class Product1_1(AbstractProduct1):

    def display(self):
        print("Inside product1_1:display()")

class Product1_2(AbstractProduct1):

    def display(self):
        print("Inside product1_2:display()")
        


class AbstractProduct2:

    def display(self):
        raise NotImplementedError("display() must defined in subclass")


class Product2_1(AbstractProduct2):

    def display(self):
        print("Inside product2_1:display()")

class Product2_2(AbstractProduct2):

    def display(self):
        print("Inside product2_2:display()")


factory1 = ConcreteFactory1()
prod1 = factory1.createProduct1()
prod1.display()
prod2 = factory1.createProduct2()
prod2.display()

factory2 = ConcreteFactory2()
prod1 = factory2.createProduct1()
prod1.display()
prod2 = factory2.createProduct2()
prod2.display()