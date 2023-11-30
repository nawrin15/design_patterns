#Step 1: Define the Handler Interface
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass
    
#Step 2: Create Concrete Handlers
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("Handled by Handler A")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("Handled by Handler B")
        else:
            print("Passed to the parent handler")
            super().handle_request(request)
     
#Step 3: Create the Chain       
class Chain:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_request(self, request):
        for handler in self.handlers:
            handler.handle_request(request)
            
#Step 4: Client Code
if __name__ == "__main__":
    chain = Chain()
    chain.add_handler(ConcreteHandlerA())
    chain.add_handler(ConcreteHandlerB())

    requests = ['A', 'B', 'C']

    for request in requests:
        print(f"Processing request: {request}")
        chain.handle_request(request)
        print()
