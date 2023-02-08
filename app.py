from flask import Flask, jsonify
import requests

app = Flask(__name__)

info = {'atencao': 'E necessario que voce insira o nome da cidade que deseja'}


@app.route('/time', methods=['GET'])
def info_inicial():
    return jsonify(info)


@app.route('/time/<name>', methods=['GET'])
def obter_dados_meteorologicos(name):
    cidade = name
    data = requests.get(
        'https://api.hgbrasil.com/weather?format=json&key=SUA-CHAVE&city_name={}'.format(cidade))

    print(type(data))
    data = data.json()
    data = data['results']
    print(data.get("city", 0))
    cidade = {'city': data.get('city'),
              'date': data.get('date'),
              'temp': data.get('temp'),
              'rain': data.get('rain'),
              'humidity': data.get('humidity')
              }
    print(cidade)

    return jsonify(cidade)


app.run(port=5000, host='localhost', debug=True)
