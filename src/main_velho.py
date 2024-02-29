from pydobot import Dobot
import json

fileLoc = "godot.json"

with open(fileLoc, "r") as arquivo:
    dados = json.load(arquivo)

dobot = Dobot(port="COM5")

# dobot.move_to_J(131.24, 212.6, 151.72, 58.31)


# def posicaoSeguranca():
#     dobot.move_to(242.23,0,151.35, 0)


# posicaoSeguranca()


entrada = "MedicamentoA"
# dobot.move_to_J(9.6, -245.3, 147.6, -87.8, wait=True)
# dobot.move_to(38.4, 0, 0, 0)



for medicamento in dados.get("medicamentos", []):
    if medicamento['nome'] == entrada:
        print(medicamento['nome'])

        for i in range(len(medicamento['posicao']['x'])):
            print(i)
            if(i == 1):
                dobot._set_end_effector_suction_cup(True)

            dobot.move_to(float(medicamento['posicao']['x'][i]),float(medicamento['posicao']['y'][i]),float(medicamento['posicao']['z'][i]),float(medicamento['posicao']['r'][i]), wait=True)

            # if(i >= 3):
            #     dobot.move_to_J(131.24, 212.6, 151.72, 58.31)
           
            # if(i == len(medicamento['posicao']['x']) - 1):
            #     dobot.move_to_J(242.2, 0, 151.3, 0)

            # dobot.wait(200)

            # if(i == len(medicamento['posicao']['x']) - 1):
            #     dobot._set_end_effector_suction_cup(False)
            if i == 2:
                #dobot._set_end_effector_suction_cup(True)
                dobot.move_to(float(medicamento['posicao']['x'][i-1]),float(medicamento['posicao']['y'][i-1]),float(medicamento['posicao']['z'][i-1]),float(medicamento['posicao']['r'][i-1]), wait=True)
            elif i == 4:
                dobot._set_end_effector_suction_cup(False)
                dobot.move_to(float(medicamento['posicao']['x'][i-1]),float(medicamento['posicao']['y'][i-1]),float(medicamento['posicao']['z'][i-1]),float(medicamento['posicao']['r'][i-1]), wait=True)

                

            dobot.wait(200)
            # print(medicamento['posicao']['x'][i])
        dobot.move_to(float(medicamento['posicao']['x'][0]),float(medicamento['posicao']['y'][0]),float(medicamento['posicao']['z'][0]),float(medicamento['posicao']['r'][0]), wait=True)
dobot.close()