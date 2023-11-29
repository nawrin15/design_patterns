import copy

class RobotPrototype:
    def clone(self):
        return copy.deepcopy(self)

class CombatRobot(RobotPrototype):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def __str__(self):
        return f"{self.name} with {self.weapon}"

# Client code
if __name__ == "__main__":
    original_robot = CombatRobot("Ranger", "Laser Blaster")
    cloned_robot = original_robot.clone()

    print(f"Original Robot: {original_robot}")
    print(f"Cloned Robot: {cloned_robot}")
    print(f"Are they the same? {original_robot is cloned_robot}")