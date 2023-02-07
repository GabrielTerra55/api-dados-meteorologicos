from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

teste = {'info': 'api_inicialmente funcionado'}

app, api = server.app, server.api

@app.route('/time')
class TimeList(Resource):
    def get (self, ):
        return teste