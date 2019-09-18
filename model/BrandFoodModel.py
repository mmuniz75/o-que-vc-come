from sql_alchemy import db, unaccent


class BrandFoodModel(db.Model):

    __tablename__ = 'brand_food'

    id_brand = db.Column(db.Integer, db.ForeignKey('brand.id'), primary_key=True)
    id_food = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)

    foods = db.relationship('FoodModel')

    def __init__(self, id_brand, id_food):
        self.id_brand = id_brand
        self.id_food = id_food

    def json(self):
        return {
            'id_brand': self.id_brand,
            'id_food': self.id_food
        }

    @classmethod
    def find_by_brand(cls, brand_id):
        return cls.query.filter_by(id_brand=brand_id)

    @classmethod
    def find_by_id(cls, brand_id, food_id):
        return cls.query.filter_by(id_brand=brand_id, id_food=food_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
