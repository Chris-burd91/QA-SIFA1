import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import User, Stock, Orders

test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
        app.config['TEST_SECRET_KEY'] = getenv('TEST_SECRET_KEY')
        return app
    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/chrisburd91/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


class TestRegistration(TestBase):

    def test_registration(self):

        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[2]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
            test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('login') in self.driver.current_url

class TestLogin(TestBase):
    
    def test_login(self):

        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
        time.sleep(1)
        
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('login') in self.driver.current_url

class TestAddOrder(TestBase):
        

    def test_add_order(self):
        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[2]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
            test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        assert url_for('login') in self.driver.current_url

        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url

        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[4]").click()
        time.sleep(5)
        
        assert url_for('add_orders') in self.driver.current_url
        time.sleep(5) 

        self.driver.find_element_by_xpath('//*[@id="product_name"]').send_keys("Test Product")
        self.driver.find_element_by_xpath('//*[@id="customer_name"]').send_keys("Test_Name")
        self.driver.find_element_by_xpath('//*[@id="customer_address"]').send_keys("Test Address")
<<<<<<< HEAD
        self.driver.find_element_by_xpath('//*[@id="order_date"]').send_keys("2020-04-032020-04-03")
=======
        self.driver.find_element_by_xpath('//*[@id="order_date"]').send_keys("2020-03-03")
>>>>>>> testing
        self.driver.find_element_by_xpath('//*[@id="order_status"]').send_keys("Test_Status")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(5) 
        
        assert url_for('add_orders') in self.driver.current_url

class TestAddStock(TestBase):

    def test_add_stock(self):
        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[2]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
            test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        assert url_for('login') in self.driver.current_url

        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[3]").click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url
        self.driver.find_element_by_xpath("/html/body/strong/nav/ul/a[6]").click()
        time.sleep(5)

        assert url_for('add_stock') in self.driver.current_url
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="product_name"]').send_keys("Test Product Name")
        self.driver.find_element_by_xpath('//*[@id="product_discription"]').send_keys("Test Discription")
        self.driver.find_element_by_xpath('//*[@id="quantity"]').send_keys("4")
        self.driver.find_element_by_xpath('//*[@id="price"]').send_keys("1232")
        self.driver.find_element_by_xpath('//*[@id="sell_price"]').send_keys("234")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(5)
        
        assert url_for('stock') in self.driver.current_url
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(port=5000)
