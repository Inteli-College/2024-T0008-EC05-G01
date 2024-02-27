from serial.tools import list_ports
from colorama import Fore, Style
# import dobotJson
# from robot import KitItem, Pos
from pydobot import Dobot


class RobotWrapper:
	def init(self):
		print(f"[{Fore.YELLOW}ROBOT{Style.RESET_ALL}] Estabelecendo conexão com o robô...")
		self.port = self.scan_ports()
		self.robot = Dobot(port=self.port) #! Depois mudar isso pra escanear portas direito no windows.
		print(f"[{Fore.YELLOW}ROBOT{Style.RESET_ALL}] Conectado ao robô na porta {Fore.GREEN}{self.port}{Style.RESET_ALL}")
		self.update_pos()
		self.inicalazed = True
	
	def __init__(self):
		self.inicalazed = False
		print("iniciando")

	def scan_ports(self) -> str:
		ports = list_ports.comports()
		for port in ports:
			# print(f"Trying port {port.device}")
			try:
				robot = Dobot(port=port.device)
				robot.close()
				# print(f"Found robot at {port.device}")
				return port.device
			except:
				print(f"No robot found at {port.device}")
		raise Exception("No robot found")

	def update_pos(self) -> None:
		self.x, self.y, self.z, self.r, self.j1, self.j2, self.j3, self.j4 = self.robot.pose()

	def move(self, x: float, y: float, z: float) -> None:
		self.robot.move_to(x, y, z, self.r, wait=True)
		self.update_pos()
	
	def move_J(self, j1: float, j2: float, j3: float, j4: float) -> None:
		self.robot.move_to_J(j1, j2, j3, j4, wait=True)
		self.update_pos()

	def current(self) -> dict[str, float]:
		self.update_pos()
		return { "x": self.x, "y": self.y, "z": self.z }

	def get_item(self, get_pos):
		self.move(get_pos.x, get_pos.y, get_pos.z)
		self.robot._set_end_effector_suction_cup(True)

	def put_item(self, put_pos):
		self.move(put_pos.x, put_pos.y, put_pos.z)
		self.robot._set_end_effector_suction_cup(False)

	def atuador_on(self):
		self.robot.suck(True)

	def atuador_off(self):
		self.robot.suck(False)