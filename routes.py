from flask import request, jsonify
from services.ChemicalService import ChemicalService
from app_flask import app

@app.route('/chemicals/<int:param_id>', methods=['PUT'])
def chemical_id(param_id):
    return ChemicalService.update_chemical(param_id, request.json['name'])


@app.route('/chemicals', methods=['GET', 'POST'])
def chemical():
    if request.method == 'GET':
        return jsonify(ChemicalService.get_chemicals())
    else:
        return ChemicalService.create_chemical(request.json['name'])
