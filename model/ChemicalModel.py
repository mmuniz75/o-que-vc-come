from sql_alchemy import db, unaccent


class ChemicalModel(db.Model):

    __tablename__ = 'chemical'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    #site = db.relationship('SiteModel')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    @classmethod
    def find_chemical(cls, chemical_id):
        chemical = cls.query.filter_by(id=chemical_id).first()
        if chemical:
            return chemical
        return None

    @classmethod
    def find_chemicals(cls):
        chemicals = cls.query.order_by(unaccent(ChemicalModel.name)).all()
        if chemicals:
            return [chemical.json() for chemical in chemicals]
        return None

    def save_chemical(self):
        db.session.add(self)
        db.session.commit()

    def update_chemical(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def delete_chemical(self):
        db.session.delete(self)
        db.session.commit()
