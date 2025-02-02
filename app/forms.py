from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import sqlalchemy as sa
from app import db
from app.models import Preprint

class RequestPreprintForm(FlaskForm):
    authors = StringField('Author(s)', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Request preprint number')

    def valide_title(self, title):
        user = db.session.scalar(sa.select(Preprint).where(Preprint.title == title.data))
        if user is not None:
            raise ValidationError('Title is already present in database. Please use a different one.')