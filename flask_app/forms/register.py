from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired(), Length(2, 45)])
    last_name = StringField("Last Name:", validators=[DataRequired(), Length(2, 45)])
    email = EmailField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired(), Length(8, 45)])
    confirm_password = PasswordField(
        "Confirm Password:", validators=[EqualTo("password", "passwords must match.")]
    )
