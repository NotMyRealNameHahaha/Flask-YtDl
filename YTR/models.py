# Models == User preferences && forms
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


# URL input form
class UrlIn(FlaskForm):
    video_url = StringField('name',
                            validators=[DataRequired()],
                            default="https://www.youtube.com/watch?v=44pTQe4Q9lg")

# Modify JSON that stores FULL path of download dir here
