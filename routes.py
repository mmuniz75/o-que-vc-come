from flask import request, jsonify
from services.ChemicalService import ChemicalService
from services.BrandService import BrandService
from services.FoodService import FoodService
from services.BrandFoodService import BrandFoodService
from services.BrandFoodChemicalService import BrandFoodChemicalService
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


@app.route('/foods/<int:param_id>', methods=['PUT'])
def food_id(param_id):
    return FoodService.update_food(param_id, request.json['name'])


@app.route('/foods', methods=['GET', 'POST'])
def foods():
    if request.method == 'GET':
        return jsonify(FoodService.get_foods())
    else:
        return FoodService.create_food(request.json['name'])


@app.route('/brand-foods/<int:brand_id>/<int:food_id>', methods=['DELETE'])
def brand_food_delete(brand_id, food_id):
    return BrandFoodService.delete(brand_id, food_id)


@app.route('/brand-foods', methods=['GET', 'POST'])
def brand_food():
    if request.method == 'GET':
        return jsonify(BrandFoodService.get_all())
    else:
        return BrandFoodService.create(request.json['brand_id'], request.json['food_id'])


@app.route('/brands/<int:param_id>/foods')
def foods_by_brand(param_id):
    return BrandService.get_foods_by_brand(param_id)


@app.route('/brands/<int:brand_id>/foods/<int:food_id>/chemicals/<int:chemical_id>', methods=['DELETE', 'POST'])
def brand_food_chemical(brand_id, food_id, chemical_id):
    if request.method == 'DELETE':
        return BrandFoodChemicalService.delete(brand_id, food_id, chemical_id)
    else:
        return BrandFoodChemicalService.create(brand_id, food_id, chemical_id)


@app.route('/brands/foods/chemicals')
def brand_food_chemicals():
    return jsonify(BrandFoodChemicalService.get_all())

