# Python imports
import os
from urllib import parse
from subprocess import run
# Dependencies
from youtube_dl import YoutubeDL
# Project Imports
from YTR.ripper import file_helpers


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


# Get the name of the video (song)
def get_name(my_url):
    with YoutubeDL({'outtmpl': '%(title)s'}) as ydl:
        video_info = ydl.extract_info(my_url, download=False)
        video_name = video_info.get('title', None)
    return my_url, video_name
    # mdl = YoutubeDL({'outtmpl': '%(title)s'})
    # video_name = mdl.extract_info(my_url, download=False)
    # return my_url, str(video_name)


# download self.link
class Dl(object):
    # Get current directory
    # cd = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()

    def __init__(self, link, name):
        self.link = link
        self.name = name

    def download(self):
        my_config = {
            'ydl_opp': {
                'format': 'mp3/mp4',
                'extractaudio': True,
                'merge_output_format': 'mp4/webm',
                'audioformat': 'mp3',
                'noplaylist': True,
                'outtmpl': '%(title)s.%(ext)s',
                'ffmpeg_location': file_helpers.find_ffmpeg(),
                'prefer_ffmpeg': True,
                'restrictfilenames': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': MyLogger(),
                # 'progress_hooks': [my_hook],
            }
        }
        with YoutubeDL(my_config) as ydl:
            ydl.download([str(self.link)])

        # Clean up main directory
        # file_helpers.clean_dir(self.name)

    # Convert video to MP3
    def convert_song(self):
        # Find this song, rename it w/ os.quote_plus
        my_video = file_helpers.find_song(which_dir=os.getcwd(),
                                          song_name=self.name)
        # Rename video to prevent FFmpeg errors
        os.rename(my_video, parse.quote_plus(my_video))

        # Get the video name + its extension
        song_name, song_ext = os.path.splitext(my_video)

        # Convert the song w/ FFmpeg
        run('ffmpeg -i "%s" -vn -ar 44100 -ac 2 -ab 200k -f mp3 "%s".mp3'
            % (parse.quote_plus(my_video), song_name),
            shell=True)

        # Move the song && video to music_dir
        # Get video
        mv = file_helpers.find_song(which_dir=os.getcwd(),
                                    song_name=parse.quote_plus(my_video))
        # Move video
        os.rename(mv, os.path.join("music", mv))
        # Remove video
        os.remove(os.path.join("music", mv))
        # Get Song
        my_song = file_helpers.find_song(which_dir=os.getcwd(),
                                         song_name=self.name)
        # Move song
        os.rename(my_song, os.path.join("music", my_song))
        # Remove video
        # os.remove(os.path.join())

    # Get songs in the music directory
    def get_songs(self):
        for ind in os.listdir(file_helpers.music_dir()):
            if self.name in ind:
                self.convert_song()
            else:
                continue

    # Send path o f


def my_test():
    northlane = "https://www.youtube.com/watch?v=IjMuhtDkN7o"
    # my_link.convert()
    north_link, north_name = get_name(northlane)
    north_video = Dl(north_link, north_name)
    north_video.download()
    # file_helpers.convert_dir()
    # north_video.file_helpers.my_converter(north_video.download())
# my_test()

