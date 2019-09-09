from flask_restful import Resource


class ChemicalResource(Resource):
    @staticmethod
    def get():
        return {"id": 1, "name": "Ácido Acético Glacial"}
