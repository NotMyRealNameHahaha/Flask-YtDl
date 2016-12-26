# Python imports
import os
# Dependencies
from youtube_dl import YoutubeDL
# Project Imports
from YTR.ripper import file_helpers
from YTR import convert


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
    mdl = YoutubeDL({'outtmpl': '%(title)s'})
    video_name = mdl.extract_info(my_url, download=False)
    return my_url, str(video_name)


# download self.link
class Dl(object):
    # Get current directory
    # cd = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    my_config = {
        'ydl_opp': {
            'format': 'mp3/best',
            'extractaudio': True,
            'merge_output_format': 'mp4/webm',
            # 'audioformat': "mp3/webm",
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

    def __init__(self, link, name):
        self.link = link
        self.name = name

    def download(self):
        with YoutubeDL(Dl.my_config) as ydl:
            ydl.download([str(self.link)])
        file_helpers.clean_dir()

    def move_file(self):
        music_dir = os.path.join(Dl.cwd, "music")
        return str(self.link + music_dir)

    # Convert video to MP3
    def convert_song(self):
        for non_songs in file_helpers.music_dir():
            if str(self.name) in non_songs:
                print("found 'em!")
            elif non_songs in str(self.name):
                print("FOUND 'EM!  The elif was the ticket")


def my_test():
    northlane = "https://www.youtube.com/watch?v=IjMuhtDkN7o"
    # my_link.convert()
    north_link, north_name = get_name(northlane)
    north_video = Dl(north_link, north_name)
    north_video.download()
    # file_helpers.convert_dir()
    # north_video.file_helpers.my_converter(north_video.download())
# my_test()

