from utils.text import printc, cstring
from tinydb import Query, TinyDB
from classes.robot import RobotWrapper
import inquirer
import yaspin
import typer
import json



app = typer.Typer()


@app.command(short_help="Executa um kit de medicamentos.", name="montar-kit")
def wrapper():
	"""
		Executa um kit de medicamentos

		Exemplo:

			$ python main.py montar_kit

			$ Escolha o medicamento do kit que você quer executar

			$ Medicamento 1

			$ Medicamento 2

			$ Medicamento 3

		Ao escolher um medicamento, o robô irá executar o kit correspondente

		Configure os kits no arquivo constants.json
	"""

	montar_kit()

def montar_kit(robot = None):
	if not robot: robot = RobotWrapper(yaspin.yaspin(color="red"))
	if not robot.initialized: robot.init()

	with open("./constants.json", "r") as arquivo:
		dados = json.load(arquivo)

	db = TinyDB('./db.json')

	# Obtém todos os registros da tabela


	kits = [medicamento['nome'] for medicamento in dados.get("medicamentos", [])]

	respostas = inquirer.prompt([
		inquirer.List("kit", message="Escolha o medicamento do kit que você quer executar", choices=kits)
	])


	#? Codigozinho do Rizzi
	for medicamento in dados.get("medicamentos", []):
		if medicamento['nome'] == respostas['kit']:
			for i in range(len(medicamento['posicao']['x'])):
				if(i == 1):
					robot.tool("suction", True)

				robot.move(float(medicamento['posicao']['x'][i]),float(medicamento['posicao']['y'][i]),float(medicamento['posicao']['z'][i]),float(medicamento['posicao']['r'][i]))

				if i == 5:
					robot.tool("suction", False)


				registros = db.all()

				# Obtém o último dado
				ultimo_dado = registros[-1]['dado']

				# Obtém o quinto dado a partir do último termo
				quinto_dado = registros[-5]['dado']

				print(ultimo_dado)
				print(quinto_dado)
				cond: bool
				if ultimo_dado > quinto_dado:
					cond = ((ultimo_dado * 1.2) <= quinto_dado) or ((ultimo_dado * 0.8) <= quinto_dado)
				elif ultimo_dado < quinto_dado:
					cond = ((ultimo_dado * 1.2) >= quinto_dado) or ((ultimo_dado * 0.8) >= quinto_dado)
				else: cond = True

				print(cond)

				if cond == False: 
					print("Objeto perdido no processo")
					break
					

	printc(cstring("[&6ROBOT&f] &aKit montado!"))