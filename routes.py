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


@app.route('/brands/<int:brand_id>/foods/<int:food_id>', methods=['DELETE', 'POST'])
def brand_food_delete(brand_id, food_id):
    if request.method == 'DELETE':
        return BrandFoodService.delete(brand_id, food_id)
    else:
        return BrandFoodService.create(brand_id, food_id, request.json['bar-code'], request.json['chemicals'])


@app.route('/brands/foods')
def brand_food():
    return jsonify(BrandFoodService.get_all())


@app.route('/foods/<int:food_id>/brands')
def brands_by_food(food_id):
    return FoodService.get_brands(food_id)

@app.route('/brands/<int:brand_id>/foods')
def foods_by_brand(brand_id):
    return BrandService.get_foods(brand_id)

@app.route('/brands/<int:brand_id>/foods/<int:food_id>/chemicals/<int:chemical_id>', methods=['DELETE', 'POST'])
def brand_food_chemical(brand_id, food_id, chemical_id):
    if request.method == 'DELETE':
        return BrandFoodChemicalService.delete(brand_id, food_id, chemical_id)
    else:
        return BrandFoodChemicalService.create(brand_id, food_id, chemical_id)


@app.route('/brands/foods/chemicals')
def brand_food_chemicals():
    return jsonify(BrandFoodChemicalService.get_all())


@app.route('/brands/<int:brand_id>/foods/<int:food_id>/chemicals')
def chemicals_by_brand_food(brand_id, food_id):
    return BrandFoodService.get_chemicals(brand_id, food_id)


@app.route('/brands/foods/<string:bar_code>/chemicals')
def brand_food_bar_code_chemicals(bar_code):
    return BrandFoodService.get_chemicals_by_barcode(bar_code)

@app.route('/brands/foods/<string:bar_code>')
def brand_food_bar_code(bar_code):
    return BrandFoodService.get_foods_brand_by_barcode(bar_code)