# Flask Stock Ticker Purchasing APP


## Initialize App Data

In flask shell run the models and create the tables
```
>>> from app import db, app
>>> from models import User, Order
>>> db.create_all()
>>>   
```
## UI (First Functional View)
![image](https://user-images.githubusercontent.com/25157436/201695812-d54f4b76-8a30-4b2c-add5-c6762613fb68.png)

## Data
_It is being populated, but selecting the ticker in the dropdown isn't working._
![image](https://user-images.githubusercontent.com/25157436/201696173-595b1ca6-a681-4c7d-8f11-5c7f9399a1ec.png)


## Bugs/Enhancements
[] Dropdown not updating to newly selected value
[] Remove hard coding of user id when creating orders (API supports multiple users and orders)
[] Yeesh, make it look nice.  Wasted time with Bootstrap CSS not loading.
