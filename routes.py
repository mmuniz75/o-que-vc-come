from flask import request, jsonify
from services.ChemicalService import ChemicalService
from services.BrandService import BrandService
from app_flask import app

@app.route('/chemicals/<int:param_id>', methods=['PUT'])
def chemical_id(param_id):
    return ChemicalService.update_chemical(param_id, request.json['name'])


@app.route('/chemicals', methods=['GET', 'POST'])
def chemicals():
    if request.method == 'GET':
        return jsonify(ChemicalService.get_chemicals())
    else:
        return ChemicalService.create_chemical(request.json['name'])


@app.route('/brands/<int:param_id>', methods=['PUT'])
def brand_id(param_id):
    return BrandService.update_brand(param_id, request.json['name'])


@app.route('/brands', methods=['GET', 'POST'])
def brands():
    if request.method == 'GET':
        return jsonify(BrandService.get_brands())
    else:
        return BrandService.create_brand(request.json['name'])