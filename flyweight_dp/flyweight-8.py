"""
    Flyweight design pattern
"""
from typing import List, Dict

class SmartPhone:
    """
    Smartphone(Flyweight)
    """
    def __init__(self, properties: List) -> None:
        self._properties = properties
        
    def sell(self, owner: str, price: int) -> None:
        """
        Selling operation on smartphone(flyweight object)
        which takes unique values per smartphone
        """
        common = self._properties
        print(f"Smartphone {common} is sold to {owner} for price {price}")
    
    def __repr__(self) -> str:
        return f"SmartPhone(properties={self._properties})"
    

class SmartPhoneFactory:
    """
    SmartPhone(flyweight) factory
    """
    _smartphones: Dict[str, SmartPhone] = {}
    
    def get_smartphone(self, properties: List)-> SmartPhone:
        """
        Return smartphone(flyweight) object
        This method creates new object and cache it if doesn't exist
        """
        key = ','.join(properties)
        if key in self._smartphones:
            print(f"Returning already existing Smartphone object for {properties}")
        else:
            print(f"New Smartphone object created for {properties}")
            self._smartphones[key] = SmartPhone(properties)
        return self._smartphones[key]
    
    def list_smartphones(self) -> List[SmartPhone]:
        """
        List down all the smartphones
        """
        smartphones = self._smartphones.values()
        for item in smartphones:
            print(item)
            

if __name__ == '__main__':
    fact = SmartPhoneFactory()
    smartphone = fact.get_smartphone(['Apple', 'iphone14', 'Black', '128 GB'])
    smartphone.sell('Sadia', 59000)
    
    smartphone = fact.get_smartphone(['Apple', 'iphone13', 'Black', '128 GB'])
    smartphone.sell('Nawrin', 49000)
    
    smartphone = fact.get_smartphone(['Samsung', 'A33', 'Black', '128 GB'])
    smartphone.sell('Shazzad', 63000)
    
    smartphone = fact.get_smartphone(['Apple', 'iphone14', 'Black', '128 GB'])
    smartphone.sell('Amit', 59000)
    
    fact.list_smartphones()