from abc import ABCMeta

class IEmployee:
    
    def showRating(self):
        pass
    
class Employee(IEmployee):
    
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        
    def showRating(self):
        print(f"Rating of {self.__name} : {self.__rating}")
        
        
class Supervisor(IEmployee):
    
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__reportees = []
        
    def showRating(self):
        print(f"Rating of {self.__name} : {self.__rating}")
        print(f"------Rating of {self.__name}'s Reportees------")
        for reportee in self.__reportees:
            reportee.showRating()
            
    def addReportee(self, employee: IEmployee):
        self.__reportees.append(employee)
        
        
if __name__ == "__main__":
    sde1 = Employee(name="Meetali", rating=4)
    sde2 = Employee(name="Sandeep", rating=3)
    pm = Supervisor(name="Sadia", rating=3)
    spm = Supervisor(name="Saroj", rating=4)
    
    pm.addReportee(sde1)
    pm.addReportee(sde2)
    
    spm.addReportee(pm)
    
    
    pm.showRating()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    spm.showRating()
    