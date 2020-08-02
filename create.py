from application import db
from application.models import Order, Stock, Users

db.drop_all()
db.create_all()
