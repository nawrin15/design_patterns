class Employee:
    
    def info(self):
        pass
    
    def salary(self):
        pass
    

class AndroidDeveloper(Employee):
    
    def info(self):
        print("I am Andriod Developer")
        return "ANDRIOD DEVELOPER"
    
    def salary(self):
        return 60000
        

class WebDeveloper(Employee):
    
    def info(self):
        print("I am web developer")
        return "WEB DEVELOPER"
        
    def salary(self):
        return 70000
        
class EmployeeAbstractFactory:
    
    def createEmployee(self):
        pass
    
class AndroidDevFactory(EmployeeAbstractFactory):
    
    def createEmployee(self):
        return AndroidDeveloper()
    
    
           
class WebDevFactory(EmployeeAbstractFactory):       
    def createEmployee(self):
        return WebDeveloper()
    
    
class EmployeeFactory:
    
    def getEmployee(self, factory: EmployeeAbstractFactory):
        return factory.createEmployee()


        
if __name__ == "__main__":
    employeeFactory = EmployeeFactory()
    employee1 = employeeFactory.getEmployee(AndroidDevFactory())
    print(f"I am {employee1.info()} and Salary: {employee1.salary()}")
    
    employee2 = employeeFactory.getEmployee(WebDevFactory())
    print(f"I am {employee2.info()} and Salary: {employee2.salary()}")
