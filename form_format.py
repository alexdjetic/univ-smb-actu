from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired

class Event(FlaskForm):
    date = DateTimeField('date: ', format='%m/%d/%y', validators=[DataRequired()])
    titre = StringField('titre: ', validators=[DataRequired()])
    description = StringField('description: ', validators=[DataRequired()])

class Commentaire(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    commentaire = StringField('commentaire', validators=[DataRequired()])

class User(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
