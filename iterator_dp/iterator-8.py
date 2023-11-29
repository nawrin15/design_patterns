from abc import ABCMeta

class MyIterator(metaclass=ABCMeta):
    
    def hasNext(self) -> bool:
        pass
    
    def next(self):
        pass
    
class MyIteratorImple(MyIterator):
    
    def __init__(self, userList) -> None:
        self.userList = userList
        self.length = len(self.userList)
        self.position = 0
        
    def hasNext(self) -> bool:
        if self.position >= self.length:
            return False
        else:
            return True
    
    def next(self):
        user = self.userList[self.position]
        self.position += 1
        return user
    
class User:
    
    def __init__(self, name, userId) -> None:
        self.name = name
        self.userId = userId
        
class UserManagement:
    
    def __init__(self) -> None:
        self.uList = []
        
    def addUser(self, user: User):
        self.uList.append(user)
        
    def getUser(self, index: int) -> User:
        return self.uList[index]
    
    def getIterator(self) -> MyIterator:
        return MyIteratorImple(self.uList)
        
userManagement = UserManagement()
userManagement.addUser(User(name="musabbih", userId=14))
userManagement.addUser(User(name="shah sulaiman", userId=34))
userManagement.addUser(User(name="murtaza", userId=97))
userManagement.addUser(User(name="musfi", userId=6))
userManagement.addUser(User(name="mahir", userId=27))

myIterator = userManagement.getIterator()

while(myIterator.hasNext()):
    user = myIterator.next()
    print(user.name)