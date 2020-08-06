from flask import render_template

from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title ='Home')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/account')
def account():
    return render_template('account.html', title='Account')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/orders')
def orders():
    return render_template('orders.html', title='Orders')

@app.route('/add_edit_orders')
def add_edit_orders():
    return render_template('add_edit_orders.html', title='Add/Edit Orders')

@app.route('/stock')
def stock():
    return render_template('stock.html', title='Stock')

@app.route('/add_edit_stock')
def add_edit_stock():
    return render_template('add_edit_stock.html', title='Add/Edit Stock')

@app.route("/logout")
def logout():

    return redirect(url_for('login'))
