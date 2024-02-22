from serial.tools import list_ports
from classes.robot import RobotWrapper
from classes.kit import KitLoader
from colorama import Fore, Style
import inquirer
import pydobot
import yaspin
import typer
import os

from commands.moveto import app as moveto_app

app = typer.Typer()
app.add_typer(moveto_app)

@app.command()
def interface():
    while True:
        perguntas_main = [
        inquirer.List("interface", message="Qual comando você quer executar ?", choices=["home", "atuador_on", "movimentar", "sair"]),
        ]

        respostas_main = inquirer.prompt(perguntas_main)
        # spinner = yaspin(text="Processando...", color="red")
        # spinner.start()
        # saida_main = processar(respostas_main)
        match respostas_main["interface"]:
            case "home":
                robot = RobotWrapper()
                robot.move(-10, 235, 140)

            case "sair":
                return
        # spinner.stop()
        # print(f"O robô se moveu para as seguintes coordenadas {saida_main}")

@app.command()
def whereami():
    robot = RobotWrapper()
    curr_pos = robot.current()

    print(f"[{Fore.YELLOW}ROBOT{Style.RESET_ALL}] Eu estou em X: {Fore.MAGENTA}{curr_pos['x']}{Style.RESET_ALL}, Y: {Fore.MAGENTA}{curr_pos['y']}{Style.RESET_ALL}, Z: {Fore.MAGENTA}{curr_pos['z']}{Style.RESET_ALL}")


@app.command('execute-kit')
def execute_kit():
    kits = [x.replace(".json", "") for x in os.listdir("kits") if x.endswith(".json")]

    perguntas = [
        inquirer.List("kit", message="Escolha o kit que você quer executar", choices=kits)
    ]

    respostas = inquirer.prompt(perguntas)
    robot = RobotWrapper()

    kit_name = respostas["kit"]

    kit_loader = KitLoader(f"kits/{kit_name}.json")
    kit_loader.execute_kit(robot)
    print(f"[{Fore.YELLOW}APP{Style.RESET_ALL}] Kit {Fore.GREEN}{kit_name}{Style.RESET_ALL} executado com sucesso!")


# def processar(dados):
#     comando = dados["interface"]

#     if comando =="high":
#         # chama a função que faz o robo se mexer para cima
#     elif comando =="down":
#         # chama a função que faz o robo se mexer para baixo
#     elif comando =="left":
#         # chama a funcão que faz o robo se mexer para esquerda
#     elif comando =="right":
#         # chama a função que faz o robo se mexer para a direita


if __name__ == "__main__":
    app()



