from flask import Flask
from flask_restful import Api
from sql_alchemy import banco
import os

from resources.ChemicalResource import ChemicalResource,ChemicalIdResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OQVC_DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(ChemicalResource, '/chemicals')
api.add_resource(ChemicalIdResource, '/chemicals/<int:id>')

@app.before_first_request
def create_db():
    banco.create_all()

if __name__ == '__main__':
    banco.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
