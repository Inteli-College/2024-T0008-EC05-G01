from classes.kit import KitLoader
from classes.robot import RobotWrapper

robot = RobotWrapper()
kit_loader = KitLoader("kits/kit1.json")
kit_loader.execute_kit(robot)
# robot.move()