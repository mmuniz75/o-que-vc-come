from sql_alchemy import db, unaccent


class BrandModel(db.Model):

    __tablename__ = 'brand'

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
    def find_brand(cls, brand_id):
        brand = cls.query.filter_by(id=brand_id).first()
        if brand:
            return brand
        return None

    @classmethod
    def find_brands(cls):
        brands = cls.query.order_by(unaccent(BrandModel.name)).all()
        if brands:
            return [brand.json() for brand in brands]
        return None

    def save_brand(self):
        db.session.add(self)
        db.session.commit()

    def update_brand(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def delete_brand(self):
        db.session.delete(self)
        db.session.commit()
