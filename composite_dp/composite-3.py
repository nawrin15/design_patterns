class Component:
    def __init__(self, name):
        self._name = name
 
    def operation(self):
        pass
 
    def add(self, component):
        pass
 
    def remove(self, component):
        pass
 
    def get_child(self, index):
        pass
 
class Leaf(Component):
    def operation(self):
        print("Leaf {}".format(self._name))
 
class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._children = []
 
    def operation(self):
        print("Composite {}".format(self._name))
        for child in self._children:
            child.operation()
 
    def add(self, component):
        self._children.append(component)
 
    def remove(self, component):
        self._children.remove(component)
 
    def get_child(self, index):
        return self._children[index]
 
composite = Composite("composite")
composite.add(Leaf("leaf1"))
composite.add(Leaf("leaf2"))
composite.operation()