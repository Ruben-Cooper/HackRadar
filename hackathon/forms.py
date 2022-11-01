
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("Username", validators=[InputRequired("Please Enter your Username")])
    email_id = StringField("Email Address", validators=[InputRequired("Please Enter your Email Address"), Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired("Please Enter your Password"),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")
    #contact Number field
    contact_number = StringField("Contact Number", validators=[InputRequired("Please Enter Contact Number")])
    # Address field
    address = StringField("Address", validators=[InputRequired("Please Enter Address")])