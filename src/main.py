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
    robot = RobotWrapper()
    while True:
        choices=["home", "atuador_on", "movimentar", "posição_atual" "sair"]

        perguntas_main = [
            inquirer.List("interface", message="Qual comando você quer executar ?", choices=choices),
        ]

        respostas_main = inquirer.prompt(perguntas_main)

        processar(respostas_main, robot, choices)

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


def processar(dados, robot, choices):
    comando = dados["interface"]

    if comando == "sair": os._exit(0)

    if robot.inicalazed == False:
        robot.init()

    if comando == "atuador_on":
        robot.atuador_on()

        if "atuador_off" not in choices:
            choices.append("atuador_off")

    match comando:
        case "home":
            robot.move(-10, 235, 140)
        
        case "atuador_off":
            robot.atuador_off()

            if "atuador_off" in choices:
                choices.remove("atuador_off")
        
        case "movimentar":
            x = float(typer.prompt("Digite a distância a ser movida no eixo X:"))
            y = float(typer.prompt("Digite a distância a ser movida no eixo Y:"))
            z = float(typer.prompt("Digite a distância a ser movida no eixo Z:"))
            
            robot.move(x,y,z) # perguntar ao gustavo qual é a função correta de movimentar

        case "posição_atual":	
            print(robot.current())

if __name__ == "__main__":
    app()



