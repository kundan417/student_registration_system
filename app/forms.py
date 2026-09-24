from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class StudentRegistrationForm(FlaskForm):

    name = StringField(
        "Student Name",
        validators=[DataRequired()]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    age = IntegerField(
        "Age",
        validators=[DataRequired(),NumberRange(min=16,max=60)]
    )

    course = SelectField(
        "Course",
        choices=[
            ("Python","Python"),
            ("Data Science","Data Science"),
            ("Machine Learning","Machine Learning"),
            ("Web Development","Web Development"),
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField("Register Student")