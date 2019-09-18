from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model.ChemicalModel import ChemicalModel
from sql_alchemy import db
from sqlalchemy.exc import IntegrityError

import logging

logger = logging.Logger('catch_all')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/oqvc')
Session = sessionmaker(bind=engine)
db.session = Session()

db.Model = declarative_base()

count = 0
chemicals = open("quimicos.txt", encoding="utf-8", newline=None)

for line in chemicals:
    chemical = line.replace("\n", "")
    model = ChemicalModel(chemical)
    try:
        db.session.flush();
        model.save_chemical()
        count = count + 1
    except IntegrityError:
        print(chemical + " already exists !")
        db.session.rollback()
    except Exception as e:
        logger.error(e, exc_info=True)
        db.session.rollback()

chemicals.close();

print("\n" + str(count) + " chemicals loaded !")






