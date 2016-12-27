# Python imports
import json
# Flask Imports
from flask import render_template, redirect, url_for, request
from flask_wtf.csrf import CsrfProtect

import YTR.models as mod
import YTR.ripper.my_YtDl
from YTR import app

CsrfProtect(app)
app.secret_key = '`\xd2\x88Z\xc6\xd6p\xc2\xab=\x1f\x02\x07\x0c\xb1'


@app.route('/')
def index():
    # Register the WTForm
    form = mod.UrlIn()
    return render_template('base_main.html', form=form)


@app.route('/dl', methods=('GET', 'POST'))
def dl():
    form = mod.UrlIn()
    if request.method == 'POST':
        user_url = form.video_url.data
        get_url, get_name = YTR.ripper.my_YtDl.get_name(user_url)
        # Set up the download class
        get_song = YTR.ripper.my_YtDl.Dl(link=get_url,
                                         name=get_name)
        # Download the bitch
        get_song.download()
        # get_song.move_file()
        get_song.convert_song()
        print("video url == ", get_name)
        print("Video name == ", get_url)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

"""
Notes:


"""