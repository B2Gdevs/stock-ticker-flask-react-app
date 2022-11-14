## Initialize App Data

In flask shell run the models and create the tables
```
>>> from app import db, app
>>> from models import User, Order
>>> db.create_all()
>>>   
```