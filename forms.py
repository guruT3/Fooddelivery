from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Optional

class SignupForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])  # <-- IMPORTANT
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    gender = SelectField("Gender", choices=["male", "female", "other"], validators=[Optional()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
  email=StringField("Email",validators=[DataRequired(),Email()])
  password=PasswordField("password",validators=[DataRequired(),Length(min=8,max=80)])
  submit=SubmitField("submit")
  
class FeedbackForm(FlaskForm):
  name=StringField("name",validators=[Optional()])
  email=StringField("Email",validators=[DataRequired(),Email()])
  feedback=StringField("feedback",validators=[DataRequired()])
  submit=SubmitField("submit")

class DeliveryInfo(FlaskForm):
  name=StringField("name",validators=[Optional()])
  email=StringField("Email",validators=[DataRequired(),Email()])
  phone_number=StringField("phone number",validators=[DataRequired()])
  address=StringField("address",validators=[DataRequired()])
  pincode=StringField("pincode",validators=[DataRequired()])
  submit=SubmitField("submit")

class Checkout(FlaskForm):
  cod=SelectField("Cash On Delivery(COD)",choices=["cod","scanner"],validators=[DataRequired()])
  submit=SubmitField("submit")

