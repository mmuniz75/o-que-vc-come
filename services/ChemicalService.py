from model.ChemicalModel import ChemicalModel

from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')


class ChemicalService:

    @staticmethod
    def get_chemicals():
        return ChemicalModel.find_chemicals()

    @staticmethod
    def create_chemical(name):
        chemical = ChemicalModel(name)
        try:
            chemical.save_chemical()

        except IntegrityError:
            return {"message": "Quimico já cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao salvar quimico"}, 500
        return chemical.json(), 201

    @staticmethod
    def update_chemical(chemical_id, name):
        chemical = ChemicalModel.find_chemical(chemical_id)
        if not chemical:
            return {"message": "Não existe quimico com id {}".format(chemical_id)}, 404

        try:
            chemical.update_chemical(name)
        except IntegrityError:
            return {"message": "Quimico já cadastrado"}, 409
        except Exception as e:
            logger.error(e, exc_info=True)
            return {"message": "Error ao alterar quimico"}, 500
        return chemical.json(), 200
