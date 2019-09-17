from sql_alchemy import banco


class ChemicalModel(banco.Model):

    __tablename__ = 'chemical'

    id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(80), unique=True)

    #site = banco.relationship('SiteModel')

    def __init__(self, id, name):
        self.id = id
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
        chemicals = cls.query.all()
        if chemicals:
            return [chemical.json() for chemical in chemicals]
        return None

    def save_chemical(self):
        banco.session.add(self)
        banco.session.commit()

    def update_chemical(self, name):
        self.name = name
        banco.session.add(self)
        banco.session.commit()

    def delete_chemical(self):
        banco.session.delete(self)
        banco.session.commit()
