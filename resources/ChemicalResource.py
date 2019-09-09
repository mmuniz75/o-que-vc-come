from flask_restful import Resource, reqparse
from model.ChemicalModel import ChemicalModel


class ChemicalResource(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('id', type=int, required=True, help="id é obrigatorio")
    atributos.add_argument('name', type=str, required=True, help="name é obrigatorio")

    @staticmethod
    def get():
        return ChemicalModel.find_chemicals()

    def post(self):
        form = ChemicalResource.atributos.parse_args();
        if ChemicalModel.find_chemical(form.id):
            return {"message": "Já existe quimico com id {}".format(form.id)}, 409
        chemical = ChemicalModel(**form)
        try:
            chemical.save_chemical()
        except:
            return {"message": "Error ao salvar quimico"}, 500
        return chemical.json(), 201

class ChemicalIdResource(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('name', type=str, required=True, help="name é obrigatorio")

    def put(self, id):
        chemical = ChemicalModel.find_chemical(id)
        if not chemical:
            return {"message": "Não existe quimico com id {}".format(id)}, 404

        form = ChemicalIdResource.atributos.parse_args();
        try:
            chemical.update_chemical(form.name)
        except:
            return {"message": "Error ao alterar quimico"}, 500
        return chemical.json(), 200

