from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Length, ValidationError, EqualTo
import re
from .models import User

# Validators for sign up form
# Email validator
def email_validator(form, field):
    
    # Regex for validate email field
    email_validate_pattern = r"^\S+@\S+\.\S+$"
    valid = re.match(email_validate_pattern, field.data)

    if valid is None:
        raise ValidationError('Indirizzo e-mail non valido.')
    else:
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Indirizzo e-mail già associato a un altro account.')

# Length validator
def length_validator(form, field):
    if len(field.data) < 1 or len(field.data) > 20:
        raise ValidationError('Il campo deve contenere da 1 a 20 caratteri.') 


# Flask form for sign up
class SignUp(FlaskForm):
    first_name = StringField(validators=[length_validator])
    last_name = StringField(validators=[length_validator])
    email = StringField(validators=[email_validator])
    password = PasswordField(validators=[length_validator, EqualTo('confirm_password', message='Le due password non coincidono')])
    confirm_password = PasswordField(validators=[length_validator, EqualTo('password', message='Le due password non coincidono')])
    submit = SubmitField('Registrati')

# Flask form for login
class Login(FlaskForm):
    email = StringField()
    password = PasswordField()
    submit = SubmitField('Accedi')

class AdminLogin(FlaskForm):
    email = StringField()
    password = PasswordField()
    submit = SubmitField('Accedi come admin')

class ReviewForm(FlaskForm):
    value = SelectField('Valutazione', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    description = TextAreaField()
    submit = SubmitField('Invia')

