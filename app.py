from flask import Flask
from flask_restful import Api

from resources.ChemicalResource import ChemicalResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ChemicalResource, '/chemicals')

if __name__ == '__main__':
    app.run(debug=True)
