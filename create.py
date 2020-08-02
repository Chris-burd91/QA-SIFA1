from application import db
from application.models import Orders, Stock, Users

db.drop_all()
db.create_all()
