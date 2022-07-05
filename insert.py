import db
from sqlalchemy.orm import sessionmaker
import random
from datetime import date


# new session
Session = sessionmaker(bind=db.engine)
session = Session()

# adding random data
for t in range(10, 20):
    item_id = random.randint(1000, 9999)
    price = random.randint(5, 50)

    tr = db.Transactions(t, str(date.today()), item_id, price)
    session.add(tr)

# save changes in database
session.commit()
