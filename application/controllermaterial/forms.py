from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, Length

class MaterialForm(FlaskForm):
    diff = StringField('diff', validators=[DataRequired(), Length(1, 10)])
    submit = SubmitField('update')