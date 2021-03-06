from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
   
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Username: ', self.username, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

     
class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    order_status = db.Column(db.String(40), default='Pending')
    customer_name = db.Column(db.String(50), nullable=False)
    customer_address = db.Column(db.String(140),nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    stock_id = db.Column('Stock',db.Integer,db.ForeignKey('stock.stock_id'))  
    def __repr__(self):
       return ''.join([
           'Order ID: ', str(self.id), '\r\n',
           'Customer Details: ', self.customer_name, '\r\n', self.customer_address, '\r\n',
           'Order Status: ', self.order_status, '\r\n'
       ])

class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_discription = db.Column(db.String(500))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.String(50), nullable=False)
    sell_price = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return ''.join([
            'Stock ID: ', str(self.id), '\r\n',
            'Product Info: ', self.product_name, '\r\n', self.product_discription, '\r\n',
            'Quantity: ',str(self.quantity), '\r\n',
            'Prices: ', 'Bought: ',str(self.price), '\r\n', 'Sold: ',str(self.sell_price), '\r\n',
        ])       
