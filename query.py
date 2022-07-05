import db
from sqlalchemy.orm import sessionmaker


# new session
Session = sessionmaker(bind=db.engine)
session = Session()

# all data
for s in session.query(db.Transactions).all():
    print(s.transaction_id, s.price)

print("*"*30)
print("Transactions with price over 35:")

# selected data
for s in session.query(db.Transactions).filter(db.Transactions.price > 35):
    print(s.transaction_id, s.price)
