# Python imports
import json
import os
from urllib import parse
import datetime
# Flask Imports
from flask import render_template, redirect, url_for, request
from flask_wtf.csrf import CsrfProtect
from flask_wtf import FlaskForm
from wtforms import BooleanField

# Project imports
import YTR.models as mod
import YTR.ripper.my_YtDl
# from YTR.ripper import file_helpers
from YTR import app

# CsrfProtect(app)
app.secret_key = '`\xd2\x88Z\xc6\xd6p\xc2\xab=\x1f\x02\x07\x0c\xb1'
music_folder = os.path.join(os.getcwd(), "YTR", "static", "music")


# Get all songs in the static/music directory
def song_dir(which_dir):
    for ind in os.listdir(which_dir):
        song_dict = {'id': parse.quote(ind),
                     # 'url': parse.quote(ind),
                     'url': parse.quote(str("static/music/" + ind)),
                     'name': ind,
                     }
        yield song_dict


@app.route('/', methods=('GET', 'POST'))
def index():
    # Register the WTForm
    form = mod.UrlIn()
    if request.method == 'POST':
        user_url = form.video_url.data
        get_url, get_name = YTR.ripper.my_YtDl.get_name(user_url)
        # Set up the download class
        get_song = YTR.ripper.my_YtDl.Dl(link=get_url,
                                         name=get_name)
        # Download the song
        get_song.download()
        get_song.convert_song()
        return redirect(url_for('songs'))
    return render_template('base_main.html', form=form)


@app.route('/songs', methods=['GET', 'POST'])
def songs():
    root_dir = os.path.basename(app.root_path)
    music_dir = os.path.join(root_dir, "static", "music")
    # music_dir = "YTR/static/music"
    # print("this dir == ", music_dir)

    # Which directory are we in?
    this_dir = mod.DeleteVideo(music_dir)
    # song_list == list of dicts
    song_list = this_dir.songdir()
    if request.method == 'POST':
        # song_names = (x['id'] for x in song_list)
        this_dir.byevideo(request.form)
        # print(json.dumps(request.form, indent=2, sort_keys=True))
        return redirect(url_for('index'))
    return render_template('base_download.html',
                           songs=song_list,
                           song_form=mod.UrlIn())

    # return render_template('base_download.html', songs=music_folder)

"""
Notes:
    Delete functionality:

"""