# Python imports
import os
import subprocess
# Dependencies
from youtube_dl import YoutubeDL, DownloadError
from asynq import async
# Project Imports
from YTR.ripper import file_helpers
from YTR.models import YtrConfig


# download self.link
class Dl(object):

    def __init__(self, link, name=None):
        self.link = link
        self.name = name

    # Get the name of the video (song)
    def song_name(self):
        with YoutubeDL({'outtmpl': '%(title)s'}) as ydl:
            video_info = ydl.extract_info(self.link, download=False)
            video_name = video_info.get('title', None)
        return video_name
        # return self.link, video_name

    @async()
    def song_dl(self):
        """
            If you would like to change download options, pass options to YoutubeDL
            Example from youtube-dl Docs:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'logger': MyLogger(),
                    'progress_hooks': [my_hook],
                }
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([str(self.link)])

        All options can be found at:  https://github.com/rg3/youtube-dl/blob/master/youtube_dl/options.py
        """
        try:
            music_dir = str(os.path.join(YtrConfig.outer_music, "%(title)s"))
            with YoutubeDL({'outtmpl': music_dir}) as ydl:
                ydl.download([str(self.link)])

        except DownloadError:
            raise DownloadError


class ConvertAll(object):
    """
        Use ConvertAll to convert any remaining videos,
            sometimes Youtube-DL is tricky
    """

    def __init__(self):
        self.self = self

    @staticmethod
    def converter(songname):
        song, song_ext = os.path.splitext(songname)
        # Get the path-safe version of song & songname
        cmd = ["ffmpeg", "-i", str(songname), "-vn", "-ar", "44100", "-ac", str(2),
               "-ab", "200k", "-f", "mp3", str(song + ".mp3")]
        subprocess.run(cmd)

    @staticmethod
    def song_getter():
        """
            Runs all of the songs in the (outer) music dir through self.converter
        """
        mdir = YtrConfig.outer_music
        getall = file_helpers.all_files(mdir)
        for ind in getall:
            song_withpath = os.path.join(mdir, ind)
            ConvertAll.converter(song_withpath)
        return True


class Cleaner:

    """
        This class helps clean up the (outer) music dir
        1. It sends mp3s to the STATIC music dir
        2. It, subsequently, removes anything that does not have .mp3 as its extension
    """
    @staticmethod
    def mover():
        """
            Step 1: Move everything with .mp3 in last 4 letters to static/music
        """
        mdir = YtrConfig.outer_music
        getall = file_helpers.all_files(mdir)

        for ind in getall:
            if "mp3" in ind[-4:]:
                # The song's current location + file name
                cur_path = os.path.join(mdir, ind)
                # The song's future name
                new_path = os.path.join(YtrConfig.static_music, ind)
                os.rename(cur_path, new_path)
                # print("YTR.ripper.downloader.Cleaner renamed", ind, " Now it's @ --> ", new_path)

    @staticmethod
    def destroyer():
        """
            Step 2:
                Remove anything in the outer music dir
                 that does NOT have ".mp3" in its last 4 letters
        """
        mdir = YtrConfig.outer_music
        getall = file_helpers.all_files(mdir)
        for ind in getall:
            this_song = os.path.join(mdir, ind)
            # Make sure mp3 is NOT in filename && it's not a directory
            if ("mp3" not in ind[-4:]) and (not os.path.isdir(this_song)):
                os.remove(this_song)
                # print("""\n YTR.ripper.downloader.Cleaner.destroyer() has removed -->""", this_song)


def test_dl():
    northlane = "https://www.youtube.com/watch?v=IjMuhtDkN7o"
    north_video = Dl(link=northlane)
    return north_video.song_dl()
# print(my_test())


def test_all():
    nl = "https://www.youtube.com/watch?v=IjMuhtDkN7o"
    nv = Dl(link=nl)
    nv.song_dl()
    ConvertAll.song_getter()
# test_all()
