import pydantic
from typing import List
from classes.Pos import Pos
from tinydb import TinyDB, Query
from fastapi import HTTPException
from fastapi.responses import JSONResponse

kits_db = TinyDB('db/kits.json')

class Kit(pydantic.BaseModel):
	class Medicamento(pydantic.BaseModel):
		nome: str
		quantidade: int
		altura: float
		pos: Pos

	nome: str
	medicamentos: List[Medicamento]

	def insert(self):
		if kits_db.search(Query().nome == self.nome) > 0:
			return HTTPException(
				status_code=401, detail="Kit já cadastrado"
			)

		else:
			kits_db.insert(self.dict())

		return

	def update(self, Nome: str):
		try:
			kits_db.update(self.dict(), Query().nome == Nome)
		except Exception as error:
			return HTTPException(
				status_code=401, detail=f"Erro ao atualizar o kit: {error}"
			)
			
		return JSONResponse(content={
			"error": False,
			"message": "Kit atualizado com sucesso"
		}, status_code=200)

	@classmethod
	def delete(cls, Nome: str):
		try:
			kits_db.remove(Query().nome == Nome)

		except Exception as error:
			return HTTPException(
				status_code=401, detail=f"Erro ao deletar o kit: {error}"
			)
		
		return JSONResponse(content={
			"error": False,
			"message": "Kit deletado com sucesso"
		}, status_code=200)

	@classmethod
	def select(cls, Nome: str):
		try:
			kit = kits_db.search(Query().nome == Nome)[0]

		except Exception as error:
			return HTTPException(
				status_code=401, detail=f"Erro ao carregar o kit: {error}"
			)

		return JSONResponse(content={
			"error": False,
			"message": "Kit carregado com sucesso",
			"kit": kit
		}, status_code=200)

	@classmethod
	def select_all(cls):
		try:
			kits = kits_db.all()

		except Exception as error:
			return HTTPException(
				status_code=401, detail=f"Erro ao carregar os kits: {error}"
			)

		return JSONResponse(content={
			"error": False,
			"message": "Kits carregados com sucesso",
			"kits": kits
		}, status_code=200)

	@classmethod
	def select_joined(cls, Nome: str):
		pass