import unittest

from flask import url_for
from flask_testing import TestCase
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application.models import User, Orders, Stock 
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
               TEST_SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        hashed_pw = bcrypt.generate_password_hash('admin2016')
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

        hashed_pw_2 = bcrypt.generate_password_hash('test2016')
        employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()




    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_homepage_view(self):
       
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_orders_view(self):
        self.client.post(url_for('login'),data=dict(email="admin@admin.com",password="admin2016"),follow_redirects=True)
        response = self.client.get(url_for('orders'))
        self.assertIn(b"Orders Page", response.data)

    def test_stock_view(self):
        self.client.post(url_for('login'),data=dict(email="admin@admin.com",password="admin2016"),follow_redirects=True)
        response = self.client.get(url_for('stock'))
        self.assertEqual(b"Stock Page", response.data)

    def test_register_view(self):

        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):

        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

class TestOrders(TestBase):

    def test_add_new_order(self):
        
        with self.client:
          self.client.post(url_for('login'),data=dict(email="admin@admin.com",password="admin2016"),follow_redirects=True)
          response = self.client.post(
             url_for('/add_orders'),
               data=dict(
                  product_name = "Test name",
                  customer_name ="Test Content",
                  custome_address = "Test content",
                  order_date = "11/11/2020",
                  order_status = "test content"
               ),
               follow_redirects=True
          )
          self.assertIn(b'Test add Order', response.data)
          self.assertEqual(response.status_code, 200)

class TestRegister(TestBase):

    def test_registration(self):
       
        with self.client:
          self.client.post(url_for('register'),follow_redirects=True)
          response = self.client.post(
                  '/register',
                  data=dict(
                      first_name="TestName",
                      last_name="TestName",
                      email = "admin@admin.com",
                      password="admin2016",
                      confirm_password ="admin2016"
                  ),
                  follow_redirects=True
              )
          self.assertIn(response.data)

class TestLogin(TestBase):
    def test_login(self):
        with self.client:
            self.client.post(url_for("login"),follow_redirects=True)
            response = self.client.post(
                    'login',
                    data=dict(
                        email="admin@admin.com",
                        password="admin2016"
                    ),
                    follow_redirects=True
                )
            self.assertEqual(current_user.email, "admin@admin.com")

