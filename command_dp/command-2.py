
class Command:
    
    def execute():
        pass 
    
class TubelightOnCommand(Command):
    
    def __init__(self, tubelight):
        self.tubelight = tubelight
        
    def execute(self):
        self.tubelight.switchOn()

class TubelightOffCommand(Command):
    
    def __init__(self, tubelight):
        self.tubelight = tubelight
        
    def execute(self):
        self.tubelight.switchOff()  
    

class RemoteController:
    
    def  __init__(self, command):
        self.command = command
        
    def setCommand(self, command):
        self.command = command
        
    def pressButton(self):
        self.command.execute()
    
class Tubelight:
    
    def switchOn(self):
        print("tubelight on")
        
    def switchOff(self):
        print("tubelight off")
        
        
tubelight = Tubelight()
tubelightOnCommand = TubelightOnCommand(tubelight)
remoteController = RemoteController(tubelightOnCommand)
remoteController.pressButton()    

tubelight = Tubelight()
tubelightOffCommand = TubelightOffCommand(tubelight)
remoteController.setCommand(tubelightOffCommand)
remoteController.pressButton()