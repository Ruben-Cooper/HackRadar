
from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import InputRequired, Length, Email, EqualTo


#creates the login information
class LoginForm(FlaskForm):
    loginusername=StringField("User Name", validators=[InputRequired('Enter user name')])
    loginpassword=PasswordField("Password", validators=[InputRequired('Enter user password')])
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

class CreateEventForm(FlaskForm):
    event_name = StringField("Event Name", validators=[InputRequired("Please Enter Event Name")])
    event_description = TextAreaField("Event Description", validators=[InputRequired("Please Enter Event Description")])
    event_date = DateField("Event Date", validators=[InputRequired("Please Enter Event Date")])
    event_image = FileField("Event Image", validators=[InputRequired("Please Enter Event Image")])
    event_location = StringField("Event Location", validators=[InputRequired("Please Enter Event Location")])
    ticket_quantity = IntegerField("Ticket Quantity", validators=[InputRequired("Please Enter Ticket Quantity")])
    ticket_price = DecimalField("Ticket Price", validators=[InputRequired("Please Enter Ticket Price")])
    event_category = SelectField("Event Category", validators=[InputRequired("Please Enter Event Category")], choices=[('Business Case Competition'), ('Business Proposals'), ('Coding Competition'), ('Datathon'), ('Hackathon'), ('Idea Pitch'), ('Robotics'), ('Seminars')])
    submit = SubmitField("Create Event")
