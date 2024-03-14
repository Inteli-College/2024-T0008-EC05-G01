from utils.text import printc, cstring
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

	kits = [medicamento['nome'] for medicamento in dados.get("medicamentos", [])]

	respostas = inquirer.prompt([
		inquirer.List("kit", message="Escolha o medicamento do kit que você quer executar", choices=kits)
	])


	#? Codigozinho do Rizzi
	for medicamento in dados.get("medicamentos", []):
		if medicamento['nome'] == respostas['kit']:
			robot.move(float(medicamento['posicao']['x']), float(medicamento['posicao']['y']), float(medicamento['posicao']['z'] + 60), float(medicamento['posicao']['r']))

			robot.move(float(medicamento['posicao']['x']), float(medicamento['posicao']['y']), float(medicamento['posicao']['z']), float(medicamento['posicao']['r']))
			robot.tool("suction", True)

			robot.move(float(medicamento['posicao']['x']), float(medicamento['posicao']['y']), float(medicamento['posicao']['z'] + 60), float(medicamento['posicao']['r']))


			robot.move(float(robot.constants['kit']['x']), float(robot.constants['kit']['y']), float(robot.constants['kit']['z'] + 60), float(robot.constants['kit']['r']))

			robot.move(float(robot.constants['kit']['x']), float(robot.constants['kit']['y']), float(robot.constants['kit']['z']), float(robot.constants['kit']['r']))
			robot.tool("suction", False)
			robot.movej_to(robot.constants['home']['x'], robot.constants['home']['y'], robot.constants['home']['z'], robot.constants['home']['r'])
	printc(cstring("[&6ROBOT&f] &aKit montado!"))
