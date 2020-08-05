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

order_stock = db.Table('order_stock',
     db.Column('order_id', db.Integer, db.ForeignKey('orders.order_id')),
     db.Column('stock_id',db.Integer, db.ForeignKey('stock.stock_id')),
     db.PrimaryKeyConstraint('order_id', 'stock_id')
)


     
class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_status = db.Column(db.String(40))
    customer_name = db.Column(db.String(50))
    customer_address = db.Column(db.String(140))
    transfer = db.relationship('order_stock', backref='Stock', lazy="dynamic")
 
    def __repr__(self):
       return ''.join([
           'Order ID: ', str(self.id), '\r\n',
           'Customer Details: ', self.customer_name, '\r\n', self.customer_address, '\r\n',
           'Order Status: ', self.order_status, '\r\n'
       ])


class Stock(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_discription = db.Column(db.String(500))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(10), nullable=False)
    sell_price = db.Column(db.Float(10), nullable=False)
  
    def __repr__(self):
        return ''.join([
            'Product ID: ', str(self.id), '\r\n',
            'Product Info: ', self.product_name, '\r\n', self.product_discription, '\r\n',
            'Quantity: ',str(self.quantity), '\r\n',
            'Prices: ', 'Bought: ',str(self.price), '\r\n', 'Sold: ',str(self.sell_price), '\r\n',
            'Serial_No.: ',str(self.serial_no)
        ])
         
