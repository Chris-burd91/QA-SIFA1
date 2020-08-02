from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime



class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
       return ''.join([
           'User ID: ', str(self.id), '\r\n',
           'Email: ', self.email, '\r\n',
           'Name: ', self.first_name, ' ', self.last_name
       ])
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    order_status = db.Column(db.String(40))
    customer_name = db.Column(db.String(50))
    customer_address = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.user_id), '\r\n'
            'Order ID: ', str(self.id), '\r\n',
            'Customer Details: ', self.customer_name, '\r\n', self.customer_address, '\r\n',
            'Time of Order: ', self.order_date, '\r\n',
            'Time of Shipping: ', self.shipped_date, '\r\n',
            'Order Status: ', self.order_status, '\r\n'
        ])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_discription = db.Column(db.String(500))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(10), nullable=False)
    sell_price = db.Column(db.Float(10), nullable=False)
    serial_no = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return ''.join([
            'Product ID: ', str(self.id), '\r\n',
            'Product Info: ', self.product_name, '\r\n', self.product_discription, '\r\n',
            'Quantity: ',str(self.quantity), '\r\n',
            'Prices: ', 'Bought: ',str(self.price), '\r\n', 'Sold: ',str(self.sell_price), '\r\n',
            'Serial_No.: ',str(self.serial_no)
        ])
            

class Order_Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)


