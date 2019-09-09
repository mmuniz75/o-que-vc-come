from flask import Flask
from model.ChemicalModel import ChemicalModel
from sql_alchemy import banco


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/oqvc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
banco.init_app(app)

model = ChemicalModel(1,"Acido Citrico")
model.save_chemical()


