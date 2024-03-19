import pydantic
from classes.Pos import Pos


class Medicamento(pydantic.BaseModel):
	nome: str
	quantidade: int
	pos: Pos

	def insert(self):
		pass

	def update(self, nome: str):
		pass

	@classmethod
	def delete(cls, Nome: str):
		pass

	@classmethod
	def select(cls, Nome: str):
		pass

	@classmethod
	def select_all(cls):
		pass