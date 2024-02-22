import json
import time
from classes.robot import RobotWrapper
from typing import List


class Pos:
	def __init__(self, x: float, y: float, z: float):
		self.x = x
		self.y = y
		self.z = z

	def offset_x(self, x: float):
		self.x += x
		return self

	def offset_y(self, y: float):
		self.y += y
		return self

	def offset_z(self, z: float):
		self.z += z
		return self


class KitItem:
	def __init__(self, name: str, pos_get: Pos, pos_put: Pos, amount: int):
		self.name = name
		self.pos_get = pos_get
		self.pos_put = pos_put
		self.amount = amount


class KitLoader:
	def __init__(self, path: str):
		try:
			with open(path) as file:
				self.data = json.load(file)
		except:
			print("Error loading file")
			self.data = {}

		self.items = self.parse_kit()



	def parse_kit(self):
		items: List[KitItem] = []
		try:
			for item, value in self.data.items():
				print(item)
				print(value)
				items.append(
					KitItem(
						item,
						Pos(value['pos_get']['x'], value['pos_get']['y'], value['pos_get']['z']), #? GetPos
						Pos(value['pos_put']['x'], value['pos_put']['y'], value['pos_put']['z']), #? PutPos
						value['amount'] #? Amount
					)
				)
		except KeyError as e:
			print(f"Error parsing kit file: {e}")
			items = []

		return items


	def execute_kit(self, robot: RobotWrapper):
		for item in self.items:
			for cur in range(item.amount):
				robot.get_item(item.pos_get.offset_z(cur*(-1))) #? Tries to get the item in a slightly lower position because we already got n items
				time.sleep(1)
				robot.put_item(item.pos_put.offset_z(cur*1)) #? Puts the item in a slightly higher position because we already put n items
				print(f"Item {item.name} #{cur+1}/{item.amount} done")
				time.sleep(2)
			print(f"Finished all {item.amount} {item.name} items")
		print("Finished all items in kit")
