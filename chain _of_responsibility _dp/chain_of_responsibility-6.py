
"The ATM Notes Dispenser Interface"
from abc import ABCMeta, abstractmethod

class IDispenser(metaclass=ABCMeta):
    "Methods to implement"
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        """Set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(amount):
        """Handle the event"""
        
"A dispenser of £10 notes"
class Dispenser10(IDispenser):
    "Dispenses £10s if applicable, otherwise continues to next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Dispensing {num} £10 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
            
"A dispenser of £20 notes"
class Dispenser20(IDispenser):
    "Dispenses £20s if applicable, otherwise continues to next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num} £20 note(s)")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
            

"A dispenser of £50 notes"
class Dispenser50(IDispenser):
    "Dispenses £50s if applicable, otherwise continues to next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num} £50 note(s)")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
            


"The ATM Dispenser Chain"
class ATMDispenserChain:  # pylint: disable=too-few-public-methods
    "The Chain Client"

    def __init__(self):
        # initializing the successors chain
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()
        # Setting a default successor chain that will process the 50s
        # first, the 20s second and the 10s last. The successor chain
        # will be recalculated dynamically at runtime.
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)       

"An ATM Dispenser that dispenses denominations of notes"
import sys

ATM = ATMDispenserChain()
AMOUNT = int(input("Enter amount to withdrawal : "))
if AMOUNT < 10 or AMOUNT % 10 != 0:
    print("Amount should be positive and in multiple of 10s.")
    sys.exit()
# process the request
ATM.chain1.handle(AMOUNT)
print("Now go spoil yourself")


        
    