from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, NumberRange

class RegisterForm(FlaskForm):
    """This class creates a form for the user """
    choices = [(str(i), str(i)) for i in range(12, 91)]

    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    age = SelectField('Age', choices=choices, validators=[DataRequired()])
    itIntention = BooleanField('Do you wish to pursue a career in IT/cyber security?', validators=[DataRequired()])
    expectation = TextAreaField('What would you like to gain from this seminar', validators=[DataRequired()])
    submit = SubmitField('Submit')


