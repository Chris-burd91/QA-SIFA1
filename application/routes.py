from flask import render_template, redirect, url_for, request

from application import app, db, bcrypt
from application.models import Users
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title ='Home Page')

@app.route('/login')
def login():
    return render_template('login.html', title ='Login Page')

@app.route('/register')
def register():
    return render_template('register.html', title ='Register Page')

@app.route('/order')
def order():
    return render_template('order.html', title ='Orders Page')

@app.route('/stock')
def stock():
    return render_template('stock.html', title ='Stock List')

@app.route('/account')
def account():
    return render_template('account.html', title ='Account Page')
