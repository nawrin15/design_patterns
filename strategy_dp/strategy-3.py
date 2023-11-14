from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """AN interface for each mood of Discount_Strategy"""

    @abstractmethod
    def give_discount(self):
        """Each class will provide its own implementation using this function."""
        pass


class FlatDiscount(DiscountStrategy):

    def give_discount(self):
        print("Flat Discount")


class CashbackDiscount(DiscountStrategy):

    def give_discount(self):
        print("Cashback Discount")


class CouponDiscount(DiscountStrategy):
    
    def give_discount(self):
        print("Coupon Discount")
    
    

class ApplyDiscount:

    def __init__(self, discount_strategy):
        """self._transport references the objects of other transport classes. Its called composition."""
        self.discount_strategy = discount_strategy

    def get_discount(self):
        """Call the operation's function from referenced instance variable."""
        self.discount_strategy.give_discount()


if __name__ == '__main__':

    flatDiscount = FlatDiscount()
    discount = ApplyDiscount(flatDiscount)
    discount.get_discount()

    cashback_discount = CashbackDiscount()
    discount = ApplyDiscount(cashback_discount)
    discount.get_discount()

    coupon_discount = CouponDiscount()
    discount = ApplyDiscount(coupon_discount)
    discount.get_discount()