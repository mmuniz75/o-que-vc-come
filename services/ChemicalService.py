from model.ChemicalModel import ChemicalModel


class ChemicalService:

    @staticmethod
    def get_chemicals():
        return ChemicalModel.find_chemicals()

    @staticmethod
    def create_chemical(chemical_id, name):
        if ChemicalModel.find_chemical(chemical_id):
            return {"message": "Já existe quimico com id {}".format(chemical_id)}, 409
        chemical = ChemicalModel(chemical_id, name)
        try:
            chemical.save_chemical()
        except 'Exception':
            return {"message": "Error ao salvar quimico"}, 500
        return chemical.json(), 201

    @staticmethod
    def update_chemical(chemical_id, name):
        chemical = ChemicalModel.find_chemical(chemical_id)
        if not chemical:
            return {"message": "Não existe quimico com id {}".format(chemical_id)}, 404

        try:
            chemical.update_chemical(name)
        except 'Exception':
            return {"message": "Error ao alterar quimico"}, 500
        return chemical.json(), 200
