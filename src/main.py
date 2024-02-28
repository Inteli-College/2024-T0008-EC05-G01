from classes.robot import RobotWrapper
from classes.kit import KitLoader
from colorama import Fore, Style
import inquirer
from yaspin import yaspin
import typer
import os

from commands.moveto import app as moveto_app

spinner = yaspin(text="Processando...", color="red")
app = typer.Typer()
app.add_typer(moveto_app)

@app.command()
def interface():
    robot = RobotWrapper()
    choices=["atuador_on", "movimentar", "montar_kit", "posição_atual", "sair"]
    while True:
        perguntas_main = [
            inquirer.List("interface", message="Qual comando você quer executar ?", choices=choices),
        ]

        respostas_main = inquirer.prompt(perguntas_main)

        choices = processar(respostas_main, robot, choices)

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

    match comando:
        case "back_home":
            spinner.start()
            robot.move(18.443, 240.97, 152.04)

            if "back_home" in choices:
                choices.remove("back_home")
            spinner.stop()

        case "atuador_on":
            spinner.start()
            robot.atuador_on()
            spinner.stop()

            if "atuador_on" in choices:
                choices.remove("atuador_on")
                choices.insert(0, "atuador_off")
        
        case "atuador_off":
            spinner.start()
            robot.atuador_off()
            spinner.stop()

            if "atuador_off" in choices:
                choices.remove("atuador_off")
                choices.insert(0, "atuador_on")
        
        case "movimentar":
            x = float(typer.prompt("Digite a distância a ser movida no eixo X:"))
            y = float(typer.prompt("Digite a distância a ser movida no eixo Y:"))
            z = float(typer.prompt("Digite a distância a ser movida no eixo Z:"))

            if "back_home" not in choices:
                choices.insert(4, "back_home")
            
            spinner.start()
            robot.move(x,y,z) 
            spinner.stop()

        case "posição_atual":	
            print(robot.current())

        case "montar_kit":
            spinner.start()
            execute_kit()
            spinner.start()

    return choices

if __name__ == "__main__":
    app()



