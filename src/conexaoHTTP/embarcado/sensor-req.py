from machine import Pin, ADC
import utime
import network
import urequests
import ujson
import time
import gc
from machine import Pin, ADC
# Pino GPIO conectado ao sensor óptico reflexivo
pino_sensor = ADC(26)

# Pino GPIO conectado ao LED
pino_led = Pin(13, Pin.OUT)

# Loop principal
#while True:
def ler_sensor():
# Ler o estado do pino
    estado_sensor = pino_sensor.read_u16()
    print(estado_sensor)
    

    # Controlar o LED com base no estado do sensor
    if estado_sensor <= 61000:
        print("Objeto: Detectado")
        pino_led.on()  # Acionar o LED (ligar)

    else:
        print("Objeto: Ausente")
        pino_led.off()  # Desligar o LED

    return estado_sensor
    # Aguardar um curto período de tempo antes de verificar novamente
    #utime.sleep(1)
    
    
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Inteli.Iot', '@Intelix10T#')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)

meu_ip = wlan.ifconfig()[0]
print(f"IP:{meu_ip}")

servidor = "http://10.128.0.12:8000"

try:
    while True:
        #requisicao de controle
        #try:
        #    response = urequests.get(f'{servidor}/status')
        #except:
        #    print("Falha na requisicao")
        # Verifica se já pode enviar os dados
        #response = urequests.get(f'{servidor}/status?ip={meu_ip}')
        #dados = response.json()
        saida_sensor = ler_sensor()
        print(f'http://{servidor}/enviando')
        response = urequests.post(url=f'{servidor}/enviando',
                                  headers = {'content-type': 'application/json'},
                                  json=ujson.dumps({
            "dado": saida_sensor,
            "ip":meu_ip
        }))
        print("DADO ENVIADO...")
        gc.collect()
        time.sleep(1)
except Exception as error:
    print("Programa Encerrado")
    print(error)
    print(type(error))

