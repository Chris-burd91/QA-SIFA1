from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime



class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True))
    username = db.Column(db.String(20), unique=True, nullable=False))
    email = db.Column(db.String(120), unique=True, nullable=False))
    password = db.Column(db.String(60), nullable=False))


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True))
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow))
    shipped_date = db.Column(db.Datetime, nullable = False, defult=datetime.utcnow))
    order_status = db.Column(db.String(40)))
    customer_name = db.Column(db.String(50)))
    customer_address = db.COloumn(db.String(140)))

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True))
    product_name = db.Column(db.String(50), nullable = False))
    product_id = db.Column(db.Integer(10), nullable = False, unique = True))
    product_discription = db.Column(db.String(500)))
    Quantity = db.Column(db.Integer(4), nullable = False))
    price = db.Column(db.Float(10), nullable = False))
    sell_price = db.Column(db.Float(10), nullable = False))
    serial_no = db.Column(db.Integer(20), unique = True, nullable = False))


