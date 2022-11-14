# import datetime
# from app import db


# class BaseModel:
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     @staticmethod
#     def rollback():
#         db.session.rollback()

#     @staticmethod
#     def commit():
#         db.session.commit()

# class User(db.Model, BaseModel):
#     id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     username = db.Column(
#         db.String,
#         unique=True)
#     orders = db.relationship('Order', backref='user')

#     def __init__(self, username: str, avatar_url: str = ''):
#         self.username = username
#         self.avatar_url = avatar_url

# # class Order(db.Model, BaseModel):
# #     id = db.Column(db.Integer, primary_key=True, unique=True)
# #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# #     ticker_name = db.Column(db.String, nullable=True)

# #     def __init__(self, user_id: int, ticker_name: str):
# #         self.user_id = user_id
# #         self.ticker_name = ticker_name



