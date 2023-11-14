class Employee:
    
    def salary(self):
        pass
    

class AndroidDeveloper(Employee):
    
    def salary(self):
        print("Getting Android developer salary")
        return 60000
        

class WebDeveloper(Employee):
    
    def salary(self):
        print("Getting Web developer salary")
        return 70000
        
        

class EmployeeFactory():
    
    def getEmployee(self, empType):
        if (None == empType) or empType == '':
            return None
        elif 'ANDROID' == empType:
            return AndroidDeveloper()
        elif 'WEB' == empType:
            return WebDeveloper()
        else:
            return None
        
        
if __name__ == "__main__":
    employeeFactory = EmployeeFactory()
    employee1 = employeeFactory.getEmployee('ANDROID')
    print(f"Salary: {employee1.salary()}")
    
    employee2 = employeeFactory.getEmployee('WEB')
    print(f"Salary: {employee2.salary()}")
    
