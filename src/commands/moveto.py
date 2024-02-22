from classes.robot import RobotWrapper
from colorama import Fore, Style
import inquirer
import typer


app = typer.Typer()

@app.command()
def moveto():
    robot = RobotWrapper()
    curr_pos = robot.current()
    print(f"[{Fore.YELLOW}ROBOT{Style.RESET_ALL}] Eu estou em X: {Fore.MAGENTA}{curr_pos['x']}{Style.RESET_ALL}, Y: {Fore.MAGENTA}{curr_pos['y']}{Style.RESET_ALL}, Z: {Fore.MAGENTA}{curr_pos['z']}{Style.RESET_ALL}")

    perguntas = [
        inquirer.Text("x", message="Digite a coordenada X"),
        inquirer.Text("y", message="Digite a coordenada Y"),
        inquirer.Text("z", message="Digite a coordenada Z")
    ]

    respostas = inquirer.prompt(perguntas)
    print(f"[{Fore.YELLOW}ROBOT{Style.RESET_ALL}] Indo para X: {Fore.MAGENTA}{respostas['x']}{Style.RESET_ALL}, Y: {Fore.MAGENTA}{respostas['y']}{Style.RESET_ALL}, Z: {Fore.MAGENTA}{respostas['z']}{Style.RESET_ALL}")
    robot.move(float(respostas["x"]), float(respostas["y"]), float(respostas["z"]))
    print(f"[{Fore.YELLOW}ROBOT{Style.RESET_ALL}] Cheguei!")