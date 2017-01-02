# Python imports
import json
import os
from urllib import parse

# Flask Imports
from flask import render_template, redirect, url_for, request, jsonify
import click

# Project imports
import YTR.models as mod
import YTR.ripper.downloader
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


# Iterate form values
def form_iter(url_list):
    for ind in url_list.values():
        if len(ind) > 5 and "youtube" in ind:
            get_url, get_name = YTR.ripper.downloader.get_name(ind)
            # Set up the Download class
            get_song = YTR.ripper.downloader.Dl(link=get_url,
                                                name=get_name)
            # Download the song
            get_song.download()
            # Convert it
            get_song.convert_song()
            # finally:
            #     return {'error_msg': str('There was an error with ', ind), 'URL': ind}


@app.route('/', methods=['GET', 'POST'])
def index():
    # Register the WTForm
    form = mod.UrlIn()
    if request.method == 'POST':
        user_url = form.data
        # Send the form data to form_iter for processing :)
        form_iter(user_url)
        return redirect(url_for('songs'))

    # Method == GET
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


@app.route('/checker', methods=['POST'])
def checker():
    # Parse the incoming JSON
    form_id = request.get_json()['input_id']
    form_url = request.get_json()['input_value']

    # Send form_url to YTR.get_name
    vid_url, vid_name = YTR.ripper.downloader.get_name(form_url)
    return_dict = {'input_id': form_id, 'video_name': vid_name}
    # return jsonify(return_dict)
    print(jsonify(**return_dict))
    return json.dumps(return_dict)


# Shutdown werkzeug server if it's interfering with other shit
@app.route('/shutdown')
def byeserver():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        pass
    func()


@app.cli.command()
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        pass
    else:
        click.echo("Shut down the server, I gotchu")
    func()

"""
Notes:
    Delete functionality:

"""