from flask import Flask, jsonify
from qreader import QReader
import cv2
import threading
import time
import json

# Create a QReader instance
qreader = QReader(
    model_size='l',
    min_confidence=0.5
)

app = Flask(__name__)

# Lista para armazenar os dados dos QR codes
qr_data_list = []

# Função para ler e armazenar os QR codes
def read_qr_codes():
    last_decoded_text = None  # Variável para armazenar o texto decodificado da última leitura
    while True:
        start_time = time.time()

        camera = cv2.VideoCapture(1)
        _, image = camera.read()
        cv2.imwrite("qrcode.png", image)
        camera.release()
        image = cv2.cvtColor(cv2.imread("qrcode.png"), cv2.COLOR_BGR2RGB)
        decoded_text = qreader.detect_and_decode(image=image)
        

        # Adicione os dados à lista apenas se o texto decodificado for diferente
        if decoded_text != last_decoded_text and decoded_text != "null":
            
            qr_data_list.append(decoded_text)
            last_decoded_text = decoded_text

        end_time = time.time()

        time_spend = end_time - start_time




        with open('dados.json', 'w') as arquivo:
            # Escreva os dados no arquivo JSON
            json.dump(qr_data_list, arquivo, indent=2)



        print(f"Tempo de processamento: {time_spend} segundos")


# Inicie a thread para ler os QR codes
qr_thread = threading.Thread(target=read_qr_codes)
qr_thread.start()

@app.route('/capture')
def get_qr_data():
    # Retorna os dados mais recentes dos QR codes
    return jsonify({"dados": qr_data_list})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
