class Television:
    
    def switchOnTV(self):
        print("TV On")
        
    def switchOffTV(self):
        print("TV Off")
        
class RoomLights:
    
    def lightsDim(self):
        print("Light Dim")
        
    def LightsBright(self):
        print("Light Bright")
        
class SoundSystem:
    
    def switchOnSoundSystem(self):
        print("Sound System is on")
        
    def switchOffSoundSystem(self):
        print("Sound System is off")
        

class HomeTheatreFacade:
    
    def __init__(self, roomLights, soundSystem, television) -> None:
        self.roomLights = roomLights
        self.soundSystem = soundSystem
        self.television = television
        
    def watchMovie(self):
        self.soundSystem.switchOnSoundSystem()
        self.television.switchOnTV()
        self.roomLights.lightsDim()
        
    def stopWatchingMovie(self):
        self.soundSystem.switchOffSoundSystem()
        self.television.switchOffTV()
        self.roomLights.LightsBright()
        
        
if __name__ == "__main__":
    soundSystem = SoundSystem()
    television = Television()
    roomLights = RoomLights()
    facade = HomeTheatreFacade(roomLights, soundSystem, television)
    facade.watchMovie()
    facade.stopWatchingMovie()