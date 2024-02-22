from pydobot import Dobot
import json

with open("medicamentos.json", "r") as arquivo:
    dados = json.load(arquivo)

dobot = Dobot(port="COM9") 



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
             if(i == 1):
                dobot._set_end_effector_suction_cup(True)

             dobot.move_to(float(medicamento['posicao']['x'][i]),float(medicamento['posicao']['y'][i]),float(medicamento['posicao']['z'][i]),float(medicamento['posicao']['r'][i]), wait=True)

             if(i >= 5):
                 dobot.move_to_J()
             
             dobot.wait(200)

             if(i == len(medicamento['posicao']['x']) - 1):
                dobot._set_end_effector_suction_cup(False)


            # print(medicamento['posicao']['x'][i]) 
dobot.close()