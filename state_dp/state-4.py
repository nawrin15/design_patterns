from abc import ABC, abstractmethod

class DoorState(ABC):
    
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class OpenState(DoorState):
    def open(self):
        print("The door is already open.")
        return self

    def close(self):
        print("Closing the door...")
        # Perform door closing process
        return ClosedState()

class ClosedState(DoorState):
    def open(self):
        print("Opening the door...")
        # Perform door opening process
        return OpenState()

    def close(self):
        print("The door is already closed.")
        return self

class Door:
    def __init__(self):
        self.current_state = ClosedState()

    def change_state(self, state):
        self.current_state = state

    def open(self):
        self.change_state(self.current_state.open())

    def close(self):
        self.change_state(self.current_state.close())

# Example usage
door = Door()

door.open() #Opening the door...
door.close() #Closing the door...
door.close() # Output: "The door is already closed."
door.open() # Output: "Opening the door..."
door.open() # Output: "The door is already open."
door.close() # Output: "Closing the door..."