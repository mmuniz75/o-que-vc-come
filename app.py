from flask import Flask, request, jsonify
from flask_restful import Api
from sql_alchemy import banco
from gevent.pywsgi import WSGIServer
import os

from services.ChemicalService import ChemicalService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OQVC_DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.route('/chemicals/<int:param_id>', methods=['PUT'])
def chemical_id(param_id):
    return ChemicalService.update_chemical(param_id, request.json['name'])


@app.route('/chemicals', methods=['GET', 'POST'])
def chemical():
    if request.method == 'GET':
        return jsonify(ChemicalService.get_chemicals())
    else:
        return ChemicalService.create_chemical(request.json['name'])


@app.before_first_request
def create_db():
    banco.create_all()


if __name__ == '__main__':
    banco.init_app(app)
    if 'OQVC_DEVELOP' in os.environ:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
