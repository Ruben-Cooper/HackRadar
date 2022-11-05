
from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import InputRequired, Length, Email, EqualTo


categories = [('Business Proposal'), ('Coding Competition'),
              ('Datathon'), ('Idea Pitch'), ('Robotics')]
status_categories = [('Unpublished'), ('Open'), ('Sold-out'), ('Cancelled')]
online_categories = [('Yes'), ('No')]
ticket_categories = [('0'), ('1'), ('2'), ('3'), ('4'),
                     ('5'), ('6'), ('7'), ('8'), ('9'), ('10')]

# creates the login information


class LoginForm(FlaskForm):
    loginusername = StringField("User Name", validators=[
                                InputRequired('Enter user name')])
    loginpassword = PasswordField("Password", validators=[
                                  InputRequired('Enter user password')])
    RememberMe = BooleanField("Remember Me")
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
    user_name = StringField("Username", validators=[
                            InputRequired("Please Enter your Username")])
    email_id = StringField("Email Address", validators=[InputRequired(
        "Please Enter your Email Address"), Email("Please enter a valid email")])
    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired("Please Enter your Password"),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")
    # contact Number field
    contact_number = StringField("Contact Number", validators=[
                                 InputRequired("Please Enter Contact Number")])
    # Address field
    address = StringField("Address", validators=[
                          InputRequired("Please Enter Address")])


class CreateEventForm(FlaskForm):
    event_name = StringField("Event Name", validators=[
                             InputRequired("Please Enter Event Name")])
    event_description = TextAreaField("Event Description", validators=[
                                      InputRequired("Please Enter Event Description")])
    event_date = DateField("Event Date", validators=[
                           InputRequired("Please Enter Event Date")])
    event_image = FileField("Event Image", validators=[
                            InputRequired("Please Enter Event Image")])
    event_location = StringField("Event Location", validators=[
                                 InputRequired("Please Enter Event Location")])
    ticket_quantity = IntegerField("Ticket Quantity", validators=[
                                   InputRequired("Please Enter Ticket Quantity")])
    ticket_price = IntegerField("Ticket Price", validators=[
                                InputRequired("Please Enter Ticket Price")])
    event_category = SelectField("Event Category", validators=[
                                 InputRequired("Please Enter Event Category")], choices=categories)
    event_status = SelectField("Event Status", validators=[
        InputRequired("Please Enter Event Status")], choices=status_categories)
    online_event = SelectField("Online Event", choices=online_categories)
    submit = SubmitField("Create Event")


class BookEventForm(FlaskForm):
    ticket_quantity = SelectField("Ticket Quantity", validators=[
        InputRequired("Please Enter Ticket Quantity")], choices=ticket_categories)
    submit = SubmitField("Book Event")
