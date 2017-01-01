# Python Imports
import os
from urllib import parse
# Dependencies
# Models == User preferences && forms
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


# URL input form
class UrlIn(FlaskForm):
    first_vid = StringField('name', default="https://www.youtube.com/watch?v=44pTQe4Q9lg")
    second_vid = StringField('name')

    third_vid = StringField('name')

    fourth_vid = StringField('name')

    fifth_vid = StringField('name')

# Modify JSON that stores FULL path of download dir here


class DeleteVideo(object):

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
        except:
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
                        print("\nYTR deleted this video:", delete_video)
                    except RuntimeError as e:
                        print("\nWell, I didn't remove this video:", os.path.join(os.getcwd(), "static", "music", ind),
                              "\n Anddddd here's the error:", e)
                else:
                    pass


# Test function
def my_test():
    music_dir = "YTR/static/music"
    my_formdata = {
                    "THY%20ART%20IS%20MURDER%20-%20Reign%20Of%20Darkness%20%28OFFICIAL%20VIDEO%29.mp3": "on",
                    "csrf_token": "1483175140##c2ade82a8012323dbb8ca760daea0d8e5d86fdf1"
                   }
    which_video = DeleteVideo(music_dir)
    which_video.byevideo(my_formdata)
# my_test()
