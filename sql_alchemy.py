from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import ReturnTypeFromArgs


class unaccent(ReturnTypeFromArgs):
    pass


db = SQLAlchemy()
