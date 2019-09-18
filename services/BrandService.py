from model.BrandModel import BrandModel
from model.BrandFoodModel import BrandFoodModel
from flask import jsonify
from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')


class BrandService:

    @staticmethod
    def get_foods_by_brand(brand_id):
        brands = BrandFoodModel.find_by_brand(brand_id)
        if len(brands.all()) == 0:
            return {"message": "Não existe alimentos para marca {}".format(brand_id)}, 404
        list = [brand.food() for brand in brands]
        return jsonify(list)

    @staticmethod
    def get_brands():
        brands = BrandModel.find_brands()
        return [brand.json() for brand in brands]

    @staticmethod
    def create_brand(name):
        brand = BrandModel(name)
        try:
            brand.save_brand()

        except IntegrityError:
            return {"message": "Marca já cadastrada"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar marca"}, 500
        return brand.json(), 201

    @staticmethod
    def update_brand(brand_id, name):
        brand = BrandModel.find_brand(brand_id)
        if not brand:
            return {"message": "Não existe marca com id {}".format(brand_id)}, 404

        try:
            brand.update_brand(name)
        except IntegrityError:
            return {"message": "Marca já cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao alterar marca"}, 500
        return brand.json(), 200
