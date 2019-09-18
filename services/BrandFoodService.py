from model.BrandFoodModel import BrandFoodModel

from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')


class BrandFoodService:


    @staticmethod
    def get_all():
        return BrandFoodModel.find_all()

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
            if not BrandFoodModel.find_by_id(brand_id, food_id):
                return {"message": "Relacionamento não cadastrado"}, 404

            relation = BrandFoodModel(brand_id, food_id)
            relation.delete()
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao remover relacionamento"}, 500
        return 204
