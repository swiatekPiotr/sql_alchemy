from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# connect with database
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
# manage tables
base = declarative_base()


class Transactions(base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    date = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)

    # constructor
    def __init__(self, transaction_id, date, item_id, price):
        self.transaction_id = transaction_id
        self.date = date
        self.item_id = item_id
        self.price = price


if __name__ == '__main__':
    base.metadata.create_all(engine)
