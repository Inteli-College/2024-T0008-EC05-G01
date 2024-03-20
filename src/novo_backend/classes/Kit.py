import pydantic
from typing import List
from classes.Pos import Pos
from tinydb import TinyDB, Query
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from database.wrapper import DB

class Kit(pydantic.BaseModel):
	class Medicamento(pydantic.BaseModel):
		nome: str
		quantidade: int
		altura: float
		pos: Pos

	nome: str
	medicamentos: List[Medicamento]

	def insert(self):
		try:
			with DB('database/archives/kits.json') as kits_db:
				if len(kits_db.search(Query().nome == self.nome)) > 0:
					return JSONResponse(content={
						"error": True,
						"message": "Kit já cadastrado"
					}, status_code=409)

				self.check_medicamentos(self.medicamentos)

				kits_db.insert(self.dict())

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao cadastrar o kit: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Kit cadastrado com sucesso"
		}, status_code=201)

	def update(self, Nome: str):
		try:
			with DB('database/archives/kits.json') as kits_db:
				if len(kits_db.search(Query().nome == self.nome)) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Kit não cadastrado"
					}, status_code=404)

				self.check_medicamentos(self.medicamentos)

				kits_db.update(self.dict(), Query().nome == Nome)

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao atualizar o kit: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Kit atualizado com sucesso"
		}, status_code=200)

	@classmethod
	def delete(cls, Nome: str):
		try:
			with DB('database/archives/kits.json') as kits_db:
				if kits_db.search(Query().nome == Nome) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Kit não cadastrado"
					}, status_code=404)

				kits_db.remove(Query().nome == Nome)

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao deletar o kit: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Kit deletado com sucesso"
		}, status_code=200)

	@classmethod
	def select(cls, Nome: str):
		try:
			with DB('database/archives/kits.json') as kits_db:
				if kits_db.search(Query().nome == Nome) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Kit não cadastrado"
					}, status_code=404)

				kit = kits_db.search(Query().nome == Nome)[0]

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao carregar o kit: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Kit carregado com sucesso",
			"kit": kit
		}, status_code=200)

	@classmethod
	def select_all(cls):
		try:
			with DB('database/archives/kits.json') as kits_db:
				kits = kits_db.all()

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao carregar os kits: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Kits carregados com sucesso",
			"kits": kits
		}, status_code=200)

	@classmethod
	def select_joined(cls, Nome: str):
		try:
			with DB('database/archives/kits.json') as kits_db:
				if kits_db.search(Query().nome == Nome) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Kit não cadastrado"
					}, status_code=404)

				kit = kits_db.search(Query().nome == Nome)[0]

		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao carregar o kit: {error}"
			}, status_code=500)

		# try:
		# 	with DB('database/archives/medicamentos.json') as medicamentos_db:
		# 		for nome_medicamento, medicamento in kit['medicamentos']:
		# 			medicamento['estoque'] = medicamentos_db.search(Query().nome == nome_medicamento)[0]

		# except Exception as error:
		# 	return JSONResponse(content={
		# 		"error": True,
		# 		"message": f"Erro ao carregar os medicamentos do kit: {error}"
		# 	}, status_code=500)

	def check_medicamentos(self, medicamentos: List[Medicamento]):
		with DB('database/archives/medicamentos.json') as medicamentos_db:
			for medicamento in medicamentos:
				if len(medicamentos_db.search(Query().nome == medicamento.nome)) <= 0:
					raise Exception(f"Medicamento {medicamento.nome} não cadastrado")
