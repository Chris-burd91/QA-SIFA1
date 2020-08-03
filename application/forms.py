from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateTimeField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users, Orders, Stock
from flask_login import current_user


class OrdersForm(FlaskForm):
    order_date = DateTimeField('Order Date:',
    validators=[
            DataRequired()
            ]
    )

    ship_date = DateField('Shipping Date:',
    validators=[
           ]
    )

    status = StringField('Order Status:',
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

    price = IntegerField('Order Amount:',
    validators=[
            DataRequired(),
            NumberRange(max=10000)
            ]
    )

class StockForm(FlaskForm):
    product_name = StringField('Product Name:',
    validators=[
            DataRequired(),
            Length(min=2, max=30)
            ]
    )

    product_Discription = TextAreaField('Product Discription:',
    validators=[
            Length(max=500)
            ]
    )

    quantity = IntegerField('Quantity in Stock:',
    validators=[
            DataRequired(),
           NumberRange(min=-15, max=10000)
            ]
    )

    bought_price = IntegerField('Price bought for:',
   validators=[
            DataRequired()
            ]
    )

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
            DataRequired(),
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
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
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
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
