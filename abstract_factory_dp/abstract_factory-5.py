
"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""
###########phone factory#############
class PhoneStore:
    
    def orderPhone(self, modelName):
        phone = Phone()
        phone = self.createPhone(modelName)
        phone.buildPhone()
        phone.assemblePhone()
        phone.packPhoneInBox()
        return phone
        
    def createPhone(self, modelName):
        pass

class IphoneFactory(PhoneStore):

    def createPhone(self, modelName):
        if modelName == "Iphone12":
            return Iphone12()
        elif modelName == "Iphone13":
            return Iphone13()
        else:
            return None
    
class OnePlusFactory(PhoneStore):

    def createPhone(self, modelName):
        if modelName == "OnePlus8":
            return OnePlus8()
        elif modelName == "OnePlus9":
            return OnePlus9()
        else:
            return None
###########phone factory#############

################Product#################
class Phone:
    def __init__(self): 
        self.brand = ""
        self.modelName = ""
        self.phoneSize = ""
        self.bodyType = ""
        
    def buildPhone(self):
        print(f"Building brand of Phone" + self.brand)
        print(f"Model Name - " + self.modelName)
        print(f"Phone Size " + self.phoneSize)
        print(f"Body made of " + self.bodyType)
    
    def assemblePhone(self):
        print("assembleing all the parts of phone.")
    
    def packPhoneInBox(self):
        print("packing of phone.")


class OnePlus8(Phone):
    def __init__(self): 
        self.brand = "oneplus"
        self.modelName = "OnePlus8"
        self.phoneSize = "5.7"
        self.bodyType = "Metalic"
    
class OnePlus9(Phone):
    def __init__(self): 
        self.brand = "oneplus"
        self.modelName = "OnePlus9"
        self.phoneSize = "5.6"
        self.bodyType = "Plastic"

class Iphone12(Phone):
    def __init__(self): 
        self.brand = "Iphone"
        self.modelName = "Iphone12"
        self.phoneSize = "5"
        self.bodyType = "Metalic"
    
class Iphone13(Phone):
    def __init__(self): 
        self.brand = "Iphone"
        self.modelName = "Iphone13"
        self.phoneSize = "5.4"
        self.bodyType = "Metalic"        

################Product#################


iphone = IphoneFactory()
iphone.orderPhone("Iphone12")

print("")

oneplus = OnePlusFactory()
oneplus.orderPhone("OnePlus8")