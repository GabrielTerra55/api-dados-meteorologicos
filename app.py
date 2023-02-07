from flask import Flask, jsonify, request
# import requests

app = Flask(__name__)

info = {'atencao': 'E necessario que voce insira o nome da cidade que deseja'}


@app.route('/time', methods=['GET'])
def info_inicial():
    return jsonify(info)


@app.route('/time/<name>', methods=['GET'])
def obter_dados_meteorologicos(name):
    cidade = name
    return "a cidade é {}".format(cidade)
    data = requests.get(
        'https://api.hgbrasil.com/weather?key=SUA-CHAVE&city_name=Campinas,SP')


app.run(port=5000, host='localhost', debug=True)


'''
# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

'''

'''@app.route("/", methods=["GET"])
def index():
	data = requests.get('https://randomuser.me/api')
	return data.json()'''
