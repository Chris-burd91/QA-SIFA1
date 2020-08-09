from flask import render_template, redirect, url_for, request, flash

from application import app, db, bcrypt
from application.models import User, Orders, Stock
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, OrdersForm, UpdateOrdersForm, StockForm, UpdateStockForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title ='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = User(
           first_name=form.first_name.data,
           last_name=form.last_name.data,
           email=form.email.data,
           password=hash_pw
           
       )
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title ='Account', form=form)



@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/orders')
@login_required
def orders():
    orderData = Orders.query.all()
    stockData = Stock.query.first()
    return render_template('orders.html', title='Orders', orders=orderData, stock=stockData)

@app.route('/add_orders', methods=['GET','POST'])
@login_required
def add_orders():
    form = OrdersForm()
    if form.validate_on_submit():
        orderData = Orders(
                order_id = Orders.order_id,
                order_status = form.order_status.data,
                customer_name = form.customer_name.data,
                customer_address = form.customer_address.data,
                order_date = form.order_date.data,
                product_name = form.product_name.data
                )

        db.session.add(orderData)
        db.session.commit()

        return redirect(url_for('orders'))
    else:
        print(form.errors)
    return render_template('add_orders.html', title='Add Orders',form=form)

@app.route("/edit_orders/<order_id>", methods=['GET','POST'])
@login_required
def edit_orders(order_id):
    order = Orders.query.filter_by(order_id=order_id).first()
    form = UpdateOrdersForm()
    if form.validate_on_submit():
        order.customer_name = form.customer_name.data
        order.customer_address = form.customer_address.data
        order.order_status = form.order_status.data
        order.product_name = form.product_name.data
        db.session.commit()
        return redirect(url_for("orders", order_id=order_id))
    elif request.method == 'GET':
        form.product_name.data = order.product_name
        form.customer_name.data = order.customer_name
        form.customer_address.data = order.customer_address
        form.order_status.data = order.order_status
    return render_template('edit_orders.html', title='Edit Orders', form=form)

@app.route("/delete_order/<order_id>")
@login_required
def delete_order(order_id):
    if current_user.is_authenticated:
        order = Orders.query.filter_by(order_id=order_id).first()
        db.session.delete(order)
        db.session.commit()
        return redirect(url_for("add_orders"))

@app.route('/stock')
@login_required
def stock():
    stockData = Stock.query.all()
    return render_template('stock.html', title='Stock', stock=stockData)

@app.route('/add_stock', methods=['GET','POST'])
@login_required
def add_stock():
    form = StockForm()
    if form.validate_on_submit():
        stockData = Stock(
                stock_id = Stock.stock_id,
                product_name = form.product_name.data,
                product_discription = form.product_discription.data,
                quantity = form.quantity.data,
                price = form.price.data,
                sell_price = form.sell_price.data
                )
        db.session.add(stockData)
        db.session.commit()
        return redirect(url_for("stock"))
    else:
        print(form.errors)
    return render_template('add_stock.html', title='Add Stock', form=form)

@app.route("/edit_stock/<stock_id>", methods=['GET','POST'])
@login_required
def edit_stock(stock_id):
    stock = Stock.query.filter_by(stock_id=stock_id).first()
    form = UpdateStockForm()
    if form.validate_on_submit():
        stock.product_name = form.product_name.data
        stock.product_discription = form.product_discription.data
        stock.quantity = form.quantity.data
        stock.price = form.price.data
        stock.sell_price = form.sell_price.data
        db.session.commit()
        return redirect(url_for("stock", stock_id=stock_id))
    elif request.method == 'GET':
        form.product_name.data = stock.product_name
        form.product_discription.data = stock.product_discription
        form.quantity.data = stock.quantity
        form.price.data = stock.price
        form.sell_price.data = stock.sell_price
    return render_template('edit_stock.html', title='Edit Stock', form=form)

@app.route("/delete_stock/<stock_id>")
@login_required
def delete_stock(stock_id):
    if current_user.is_authenticated:
        stock = Stock.query.filter_by(stock_id=stock_id).first()

        db.session.delete(stock)
        db.session.commit()
        return redirect(url_for("add_stock"))

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = User.query.filter_by(id=user).first()
    logout_user()
      
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))
