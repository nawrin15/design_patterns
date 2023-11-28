from abc import ABC, abstractmethod


class OrderProcessingTemplate(ABC):
    
    def __init__(self):
        self.isGiftWrap = False


    @abstractmethod
    def selectProduct(self) -> None:
        pass

    @abstractmethod
    def makePayment(self) -> None:
        pass
    
    def packProduct(self) -> None:
        if self.isGiftWrap:
            print("Gift Wraping Product")
        else:
            print("Simply Packed product") 

    @abstractmethod
    def deliverProduct(self) -> None:
        pass
    
    def processOrder(self) -> None:
        self.selectProduct()
        self.makePayment()
        self.packProduct()
        self.deliverProduct()


class StoreOrder(OrderProcessingTemplate):

    def selectProduct(self) -> None:
        print("Selecting product on store")

    def makePayment(self) -> None:
        print("Making cash/card payment at store")

    def deliverProduct(self) -> None:
        print("Product delivered to customer")
        
class OnlineOrder(OrderProcessingTemplate):
    def selectProduct(self) -> None:
        print("Selecting product and adding to cart")

    def makePayment(self) -> None:
        print("Making COD or online payment at website/app")

    def deliverProduct(self) -> None:
        print("Product dispatched")


if __name__ == "__main__":
    storeOrder = StoreOrder()
    storeOrder.processOrder()
    print("\n")
    onlineOrder = OnlineOrder()
    onlineOrder.isGiftWrap = True
    onlineOrder.processOrder()