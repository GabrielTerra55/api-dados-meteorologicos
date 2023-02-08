from flask import Flask, jsonify
import requests

app = Flask(__name__)

info = {'atencao': 'E necessario que voce insira o nome da cidade que deseja'}
erro = {'atencao': 'Pode ter ocorrido um erro de digitacao com o municipio desejado! tente novamente',
        'observacao': 'Se o municipio escolhido foi Sao Paulo, ignore o aviso'
}



@app.route('/time', methods=['GET'])
def info_inicial():
    return jsonify(info)


@app.route('/time/<name>', methods=['GET'])
def obter_dados_meteorologicos(name):
    nome_cidade = name
    data = requests.get(
        'https://api.hgbrasil.com/weather?format=json&key=SUA-CHAVE&city_name={}'.format(nome_cidade))

    data = data.json()
    data = data['results']
    cidade = {'city': data.get('city'),
              'date': data.get('date'),
              'temp': data.get('temp'),
              'rain': data.get('rain'),
              'humidity': data.get('humidity')
              }
    print(data['city'])
   
    if cidade['city'] != 'São Paulo, SP':
        return jsonify(cidade)

    return jsonify(cidade, erro)

if __name__ == '__main__':
    app.run()
