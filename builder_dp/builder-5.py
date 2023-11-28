class Director:
    
    def __init__(self) -> None:
        self.builder = None
        
    def setBuilder(self, builderObj):
        self.builder = builderObj
        
    def Construct(self, name):
        if name == 'Product1':
            self.builder.create()
            self.builder.buildPartA()
            self.builder.buildPartB()
        elif name == 'Product2':
            self.builder.create()
            self.builder.buildPartC()
            self.builder.buildPartD()
            
class Builder:
    
    def create(self):
        raise NotImplementedError('create() must be defined in subclass')
    
    def buildPartA(self):
        raise NotImplementedError('buildPartA() must be defined in subclass')
    
    def buildPartB(self):
        raise NotImplementedError('buildPartB() must be defined in subclass')
    
    def buildPartC(self):
        raise NotImplementedError('buildPartC() must be defined in subclass')
    
    def buildPartD(self):
        raise NotImplementedError('buildPartD() must be defined in subclass')
    
    
class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.product = None
        
    def create(self):
        self.product = Product1()
        
    def buildPartA(self):
        pass
    
    def buildPartB(self):
        pass       
    
    def buildPartC(self):
        pass
    
    def buildPartD(self):
        pass
    
    def getProduct(self):
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self) -> None:
        self.product = None
        
    def create(self):
        self.product = Product2()
        
    def buildPartA(self):
        pass
    
    def buildPartB(self):
        pass       
    
    def buildPartC(self):
        pass
    
    def buildPartD(self):
        pass
    
    def getProduct(self):
        return self.product
    
class Product1:
    def useProduct(self):
        print("Inside Product1:useProduct()")
        
class Product2:
    def useProduct(self):
        print("Inside Product2:useProduct()")
        
        
director = Director()

builder1 = ConcreteBuilder1()
director.setBuilder(builder1)
director.Construct('Product1')
prod1 = builder1.getProduct()
prod1.useProduct()

builder2 = ConcreteBuilder2()
director.setBuilder(builder2)
director.Construct('Product2')
prod2 = builder2.getProduct()
prod2.useProduct()