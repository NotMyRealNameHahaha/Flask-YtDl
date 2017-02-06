# Python Imports
import os
from urllib import parse
# Dependencies
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

"""
    models.py contains:
        - Forms
        - Methods behind the 'delete' functionality of the "my music" page
"""


# URL input form
class UrlIn(FlaskForm):
    first_vid = StringField('name', default="https://www.youtube.com/watch?v=44pTQe4Q9lg")
    second_vid = StringField('name')

    third_vid = StringField('name')

    fourth_vid = StringField('name')

    fifth_vid = StringField('name')


class CrudMethod(object):

    def __init__(self, which_dir):
        self.which_dir = which_dir

    # Get list of files in which_dir
    def songdir(self):
        for ind in os.listdir(self.which_dir):
            song_dict = {'id': parse.quote(ind),
                         'url': parse.quote(str("static/music/" + ind)),
                         'name': ind,
                         'bool_input': BooleanField(default=False)
                         }
            yield song_dict

    # Delete video function
    def byevideo(self, vid_name):
        # vid_name = request.form
        # vid_name == { "parse.quote(name_of_my_song)": "on", "parse.quote(other_song)": "on"}
        # First, remove "csrf_token" from vid_name
        try:
            del vid_name["csrf_token"]
        except KeyError:
            pass
        rihanna = os.path.join(os.getcwd(), self.which_dir)
        # Loop the music_dir
        for ind in os.listdir(rihanna):
            for url_key in vid_name.keys():
                # print(url_key)
                if ind == parse.unquote(url_key):
                    try:
                        delete_video = os.path.join(rihanna, ind)
                        # print(delete_video)
                        os.remove(delete_video)
                        # print("\nYTR deleted this video:", delete_video)
                    except RuntimeError as e:
                        print("\nWell, I didn't remove this video:", ind,
                              "\n And it threw this error:", e)
                else:
                    pass

