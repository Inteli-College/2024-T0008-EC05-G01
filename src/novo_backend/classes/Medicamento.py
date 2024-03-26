import pydantic
from classes.Pos import Pos
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from tinydb import TinyDB, Query
from database.wrapper import DB

class Medicamento(pydantic.BaseModel):
	nome: str
	quantidade: int
	pos: Pos

	def insert(self):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				if len(medicamentos_db.search(Query().nome == self.nome)) > 0:
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento já cadastrado"
					}, status_code=409)

				medicamentos_db.insert(self.dict())
		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao cadastrar o medicamento: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamento inserido com sucesso"
		}, status_code=201)

	def update(self, nome: str):
		try: # tenta mexer no db
			with DB('database/archives/medicamentos.json') as medicamentos_db: # abre o db
				if len(medicamentos_db.search(Query().nome == nome)) <= 0:
					# erro nosso, criado pelo programador
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento não encontrado"
					}, status_code=404)

				medicamentos_db.update(self.dict(), Query().nome == nome)

			# fechou o db
		except Exception as error:
			# erro do sistema, jogado pelo python mas a gente trata antes de parar o app
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao atualizar o medicamento: {error}"
			}, status_code=500)

		# caso de sucesso, pq  se ele chegou aqui (ainda nao retornou), nada deu errado
		return JSONResponse(content={
			"error": False,
			"message": "Medicamento atualizado com sucesso"
		}, status_code=200)

	@classmethod
	def delete(cls, Nome: str):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamentos_db.remove(Query().nome == Nome)
		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao deletar o medicamento: {error}"
			}, status_code=500)

	@classmethod
	def select(cls, Nome: str):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamento = medicamentos_db.search(Query().nome == Nome)
				if len(medicamento) <= 0:
					return JSONResponse(content={
						"error": True,
						"message": "Medicamento não encontrado"
					}, status_code=404)

				medicamento = medicamento[0]
		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao buscar o medicamento: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamento encontrado com sucesso",
			"medicamento": medicamento
		}, status_code=200)

	@classmethod
	def select_all(cls):
		try:
			with DB('database/archives/medicamentos.json') as medicamentos_db:
				medicamentos = medicamentos_db.all()
		except Exception as error:
			return JSONResponse(content={
				"error": True,
				"message": f"Erro ao buscar os medicamentos: {error}"
			}, status_code=500)

		return JSONResponse(content={
			"error": False,
			"message": "Medicamentos encontrados com sucesso",
			"medicamentos": medicamentos
		}, status_code=200)