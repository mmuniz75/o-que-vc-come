from model.BrandFoodModel import BrandFoodModel
from model.BrandFoodChemicalModel import BrandFoodChemicalModel
from flask import jsonify
from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')


class BrandFoodService:

    @staticmethod
    def get_chemicals(brand_id, food_id):

        relation = BrandFoodModel.find_by_id(brand_id, food_id)
        if not relation:
            return {"message": "Marca e produto não cadastrado"}, 404

        chemicals = BrandFoodChemicalModel.find_by_brand_food(brand_id, food_id)
        if len(chemicals.all()) == 0:
            return {"message": "Não existe quimicos para alimento {} da marca {}".format(brand_id, food_id)}, 404

        chemical_list = [chemical.chemical_name() for chemical in chemicals]
        return jsonify(chemical_list)

    @staticmethod
    def get_all():
        relations = BrandFoodModel.find_all()
        return [relation.json() for relation in relations]

    @staticmethod
    def create(brand_id, food_id):
        relation = BrandFoodModel(brand_id, food_id)
        try:
            relation.save()

        except IntegrityError:
            return {"message": "Relacionamento já cadastrado ou alimento/marca não cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar relacionamento"}, 500
        return relation.json(), 201

    @staticmethod
    def delete(brand_id, food_id):
        try:
            relation = BrandFoodModel.find_by_id(brand_id, food_id)
            if not relation:
                return {"message": "Relacionamento não cadastrado"}, 404

            relation.delete()
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao remover relacionamento"}, 500
        return {}, 204
