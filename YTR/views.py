# Python imports
import json
import os
from urllib import parse
from threading import Thread
from operator import itemgetter
# Dependencies
from flask import render_template, redirect, url_for, request
import click
from youtube_dl import YoutubeDL, DownloadError

# Project imports
import YTR.models as mod
from YTR.ripper import downloader
from YTR import app

# CsrfProtect(app)
app.secret_key = '`\xd2\x88Z\xc6\xd6p\xc2\xab=\x1f\x02\x07\x0c\xb1'
# app.jinja_env(auto_reload=True)
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


# Conversion & Cleanup callback
def cleanup():
    downloader.ConvertAll.song_getter()
    downloader.Cleaner.mover()
    # downloader.Cleaner.destroyer()


def god(vurl):
    get_song = downloader.Dl(link=vurl)
    get_song.song_dl()
    downloader.ConvertAll.song_getter()
    downloader.Cleaner.mover()
    downloader.Cleaner.destroyer()


@app.route('/', methods=['GET', 'POST'])
def index():
    # Register the WTForm
    form = mod.UrlIn()
    if request.method == 'POST':
        # print(request.data)
        reqdta = request.get_json(force=True)
        # print(reqdta)
        try:
            # get_song = downloader.Dl(link=reqdta['input_value'])
            # get_song.song_dl()
            # thrd = Thread(target=cleanup())
            # thrd.start()
            Thread(target=god(reqdta['input_value'])).start()
            return_dict = {"input_id": reqdta['input_id'], 'worked': True, 'song_name': "song"}
            return json.dumps(return_dict)

        except DownloadError:
            return_dict = {'input_id': reqdta['input_id'], 'worked': False}
            return json.dumps(return_dict)

    # Method == GET
    return render_template('base_main.html', form=form)


@app.route('/checker', methods=['POST'])
def checker():
    # Parse the incoming JSON
    form_id = request.get_json()['input_id']
    form_url = request.get_json()['input_value']
    # print("The element ID was -> ", form_id,
    #       "\nVideo URL was -->", form_url)

    # Use some YoutubeDL magic real quick
    try:
        with YoutubeDL({'outtmpl': '%(title)s'}) as ydl:
            video_info = ydl.extract_info(form_url, download=False)
            video_name = video_info.get('title', None)
        # Return dict w/ that input_id & the name (title) of the video
        return_dict = {'input_id': form_id, 'video_name': video_name}
        return json.dumps(return_dict)

    # If the URL is incorrect...
    except DownloadError:
        return json.dumps({"input_id": form_id, "error": "Double check that URL."})


@app.route('/songs', methods=['GET', 'POST'])
def songs():
    root_dir = os.path.basename(app.root_path)
    music_dir = os.path.join(root_dir, "static", "music")
    # music_dir = "YTR/static/music"

    # Which directory are we in?
    this_dir = mod.CrudMethod(music_dir)
    # song_list == list of dicts
    song_list = this_dir.songdir()
    if request.method == 'POST':
        # song_names = (x['id'] for x in song_list)
        # print(request.form)
        # print(dict(request.form))
        this_dir.byevideo(request.form)
        return redirect(url_for('songs'))
    return render_template('base_download.html',
                           songs=sorted(song_list, key=itemgetter("name")),
                           song_form=mod.UrlIn())


# Shutdown werkzeug server
@app.route('/shutdown')
def byeserver():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        pass
    func()


# shutdown.sh uses this to shut down server
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