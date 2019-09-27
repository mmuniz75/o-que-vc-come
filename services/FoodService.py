from model.FoodModel import FoodModel

import logging

logger = logging.Logger('catch_all')


class FoodService:

    @staticmethod
    def get_foods():
        foods = FoodModel.find_foods()
        return [food.json() for food in foods]

    @staticmethod
    def create_food(name):
        food = FoodModel(name)
        try:
            if FoodModel.find_by_name(name):
                return {"message": "Alimento já cadastrado"}, 409

            food.save_food()

        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar alimento"}, 500
        return food.json(), 201

    @staticmethod
    def update_food(food_id, name):
        food = FoodModel.find_food(food_id)
        if not food:
            return {"message": "Não existe alimento com id {}".format(food_id)}, 404

        try:
            food.update_food(name)
        except IntegrityError:
            return {"message": "Alimento já cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao alterar alimento"}, 500
        return food.json(), 200
