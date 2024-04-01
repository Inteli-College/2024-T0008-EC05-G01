from tinydb import Query

from modules.robot.classes.robot import RobotWrapper
from modules.robot.classes.Kit import Kit
from modules.robot.classes.Pos import Pos
from database.wrapper import DB


class KitAssembler:
	robot = RobotWrapper(auto_init=True)

	def __init__(self):
		pass


	def get_pos(self):
		"""
			Retorna a posição atual do robô
		"""
		return self.robot.current()

	def assemble(self, kit: dict):
		"""
			Recebe um kit e monta ele
		"""
		try: kit = Kit(kit)
		except Exception as e: raise Exception(f"Erro ao criar o kit: {e}")

		with DB('database/archives/kits.json') as kits_db:
			if len(kits_db.search(Query().nome == kit.nome)) <= 0:
				raise Exception("Kit não cadastrado")

		for medicamento in kit.medicamentos:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamento_estoque = medicamentos_db.search(Query().nome == medicamento.nome)

			if len(medicamento_estoque) <= 0:
				raise Exception(f"Medicamento {medicamento.nome} não cadastrado")

			medicamento_estoque = medicamento_estoque[0]
			get_pos = Pos(
				medicamento_estoque['pos']['x'],
				medicamento_estoque['pos']['y'],
				medicamento_estoque['pos']['z'],
				medicamento_estoque['pos']['r']
			)

			put_pos = Pos(
				medicamento.pos.x,
				medicamento.pos.y,
				medicamento.pos.z,
				medicamento.pos.r
			)

			for i in range(0, medicamento.quantidade):
				print(f"Montando {medicamento.nome} {i + 1}/{medicamento.quantidade}")
				self.assemble_medication(
					put_pos.offset_z(i * medicamento.altura),
					# look forward, get_pos is the pos of the last one so that one should be offset_z 0
					get_pos.offset_z(medicamento.quantidade-i * medicamento.altura)
				)

		self.robot.home()



	def assemble_medication(self, put_pos: Pos, get_pos: Pos):
		"""
			Recebe um medicamento e monta ele
		"""
		self.robot.move_safe(get_pos.x, get_pos.y, get_pos.z)

		self.robot.tool("suction", True)

		self.robot.move_safe(put_pos.x, put_pos.y, put_pos.z)

		self.robot.tool("suction", False)