from sqlalchemy import text

from sql_alchemy import db, unaccent


class BrandFoodModel(db.Model):

    __tablename__ = 'brand_food'

    id_brand = db.Column(db.Integer, db.ForeignKey('brand.id'), primary_key=True)
    id_food = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)

    bar_code = db.Column(db.Integer, nullable=False, unique=True, index=True)

    foods = db.relationship('FoodModel', lazy='joined')

    def __init__(self, id_brand, id_food, bar_code):
        self.id_brand = id_brand
        self.id_food = id_food
        self.bar_code = bar_code

    def json(self):
        return {
            'id_brand': self.id_brand,
            'id_food': self.id_food,
            'bar_code': self.bar_code
        }

    def food(self):
        food = self.foods.json()
        return {
            'bar-code': self.bar_code,
            'food-id': food['id'],
            'food': food['name']
        }

    @classmethod
    def find_by_brand(cls, brand_id):
        return cls.query.filter_by(id_brand=brand_id).order_by(unaccent(text("name")))

    @classmethod
    def find_by_id(cls, brand_id, food_id):
        return cls.query.enable_eagerloads(False).filter_by(id_brand=brand_id, id_food=food_id).first()

    @classmethod
    def find_by_bar_code(cls, bar_code):
        return cls.query.enable_eagerloads(False).filter_by(bar_code=bar_code).first()

    @classmethod
    def find_all(cls):
        return cls.query.enable_eagerloads(False).all()

    def save(self):
        db.session.add(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
