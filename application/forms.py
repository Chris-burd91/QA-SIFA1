from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField, TextAreaField, FloatField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField
from application.models import User, Orders
from flask_login import current_user


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
    validators=[
        DataRequired(),
        Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
    validators=[
        DataRequired(),
        Length(min=3, max=30)
         ]

    )

    email = StringField('Email',
    validators = [
        DataRequired(),
        Email()
        ]
    )

    password = PasswordField('Password',
        validators = [
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already Exists!')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ])

    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')

class OrdersForm(FlaskForm):
    
    product_name = StringField('Product:',
    validators=[
            Length(min=2, max=50)
            ]
    )
    

    order_status = StringField('Order Status:',
    validators=[
            Length(min=2, max=50)
            ]
    )

    customer_name = StringField('Customer Name:',
    validators=[
            DataRequired(),
            Length(min=2, max=60)
            ]
    )

    customer_address = TextAreaField('Customer Address:',
    validators=[
            DataRequired(),
            Length(max=500)
            ]
    )
    order_date = DateField('Date of Order: ',format='%Y-%m-%d',
    validators=[
            DataRequired(),
            ]
    )

    submit = SubmitField('Send Order')

class UpdateOrdersForm(FlaskForm):

    product_name = StringField('Product:',
    validators=[
            Length(min=2,max=50),
            DataRequired()
            ]
    )
    
    order_status = StringField('Order Status:',
    validators=[
            Length(min=2, max=50)
            ]
    )
    customer_name = StringField('Customer Name:',
    validators=[
            DataRequired(),
            Length(min=2, max=60)
            ]
    )
    customer_address = TextAreaField('Customer Address:',
    validators=[
            DataRequired(),
            Length(max=500)
            ]
    )
    submit = SubmitField('Update Order')


class StockForm(FlaskForm):

    product_name = StringField('Proctuct Name:',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
            ]
        )
    product_discription = TextAreaField('Product Discription:', validators=[Length(min=0, max=500)])

    quantity = StringField('Quantity:', 
        validators=[
            DataRequired(),
            ]
        )
    price = StringField('Bought Price:', 
        validators=[
            DataRequired(),
            ]
        )
    sell_price = StringField('Sold Price:',
        validators=[
            DataRequired()
            ]
        )
    submit = SubmitField('Add Stock')


class UpdateStockForm(FlaskForm):

    product_name = StringField('Proctuct Name:',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
            ]
        )
    product_discription = TextAreaField('Product Discription:', validators=[Length(min=0, max=500)])

    quantity = StringField('Quantity:', 
        validators=[
            DataRequired()
            ]
        )
    price = StringField('Bought Price:', 
        validators=[
            DataRequired(),
            ]
        )
    sell_price = StringField('Sold Price:',
        validators=[
            DataRequired(),
            ]
        )
    submit = SubmitField('Update Stock')             
