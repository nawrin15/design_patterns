class Mobile:
    
    def createMobile(self):
        pass
    

class Iphone(Mobile):
    
    def createMobile(self):
        print("creating Iphone mobile phone.")
        

class OnePlus(Mobile):
    
    def createMobile(self):
        print("creating One plus mobile phone.")
        
class Realme(Mobile):
    
    def createMobile(self):
        print("creating Realme mobile phone.")
        

class MobileFactory():
    
    def createMobile(self, companyName):
        if (None == companyName) or companyName == '':
            return None
        elif 'IPHONE' == companyName:
            return Iphone()
        elif 'ONEPLUS' == companyName:
            return OnePlus()
        elif 'REALME' == companyName:
            return Realme()
        else:
            return None
        
        
if __name__ == "__main__":
    mobileFactory = MobileFactory()
    mobile = mobileFactory.createMobile('IPHONE')
    mobile.createMobile()
    
    mobile = mobileFactory.createMobile('ONEPLUS')
    mobile.createMobile()
    
    mobile = mobileFactory.createMobile('REALME')
    mobile.createMobile()