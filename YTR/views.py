# Python imports
import json
import os
from urllib import parse
# Flask Imports
from flask import render_template, redirect, url_for, request
from flask_wtf.csrf import CsrfProtect

import YTR.models as mod
import YTR.ripper.my_YtDl
from YTR import app

CsrfProtect(app)
app.secret_key = '`\xd2\x88Z\xc6\xd6p\xc2\xab=\x1f\x02\x07\x0c\xb1'
music_folder = os.path.join(os.getcwd(), "YTR", "static", "music")


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
        return redirect(url_for('dl'))
    return render_template('base_main.html', form=form)


@app.route('/song')
def dl():
    # Register the WTForm
    form = mod.UrlIn()
    music_dir = os.path.join(os.getcwd(), "YTR", "static", "music")
    print(os.listdir(music_dir)[0],
          str("URL encoded == " + parse.quote(os.listdir(music_dir)[0])))
    song_url = os.path.join(url_for('static', filename="music"),
                            parse.quote(os.listdir(music_dir)[0]))
    song_name = os.listdir(music_dir)[0]
    return render_template('base_download.html',
                           song_name=song_name,
                           song_url=song_url,
                           form=form)
    # return render_template('base_download.html', songs=music_folder)

"""
Notes:


"""