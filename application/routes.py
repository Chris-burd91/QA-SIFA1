from flask import render_template, redirect, url_for, request, flash

from application import app, db, bcrypt
from application.models import User
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm
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
    return render_template('orders.html', title='Orders')

@app.route('/add_edit_orders')
@login_required
def add_edit_orders():
    return render_template('add_edit_orders.html', title='Add/Edit Orders')

@app.route('/stock')
@login_required
def stock():
    return render_template('stock.html', title='Stock')

@app.route('/add_edit_stock')
@login_required
def add_edit_stock():
    return render_template('add_edit_stock.html', title='Add/Edit Stock')

@app.route("/account/delete", methods=["GET", "POST"])
@login_required
def account_delete():
    user = current_user.id
    account = User.query.filter_by(id=user).first()
    logout_user()
      
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))
