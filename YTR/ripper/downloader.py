# Python imports
import os
from subprocess import run
# Dependencies
from youtube_dl import YoutubeDL
# Project Imports
from YTR.ripper import file_helpers


class YtrLogger(object):
    def debug(self, msg):
        yield ('\nDegug -> ', msg, '  From: ', self)

    def warning(self, msg):
        yield ('\nWarning -> ', msg, '  From: ', self)

    def error(self, msg):
        yield ('Error:', msg, '  From: ', self)


def ytr_hook(d):
    if d['status'] == 'finished':
        yield ('Done downloading, now converting ...')


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
        music_dir = str(os.path.join("music", "%(title)s"))
        ydl_ops = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '200'
            }],
            'outtmpl': music_dir,
            'logger': YtrLogger(),
            'progress_hooks': [ytr_hook]
        }
        with YoutubeDL(ydl_ops) as ydl:
            ydl.download([str(self.link)])
        # return self.name
        yield YtrLogger(),


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
        # Run it through FFmpeg
        run('ffmpeg -i "%s" -vn -ar 44100 -ac 2 -ab 200k -f mp3 "%s".mp3 | ffmpeg'
            % (songname, song),
            shell=True)

    def song_getter(self):
        """
            Runs all of the songs in the (outer) music dir through self.converter
        """
        mdir = file_helpers.music_dir()
        getall = file_helpers.all_files(mdir)
        for ind in getall:
            if ".mp3" not in ind[-4:]:
                song_withpath = os.path.join(mdir, ind)
                self.converter(song_withpath)


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
        mdir = file_helpers.music_dir()
        getall = file_helpers.all_files(mdir)
        # Get the static music dir
        stat_mdir = os.path.join(os.getcwd(), "YTR", "static", "music")
        # print("static music dir is at ->", stat_mdir)
        for ind in getall:
            # sname, sext = os.path.splitext(ind)
            if "mp3" in ind[-4:]:
                # The song's current location
                cur_path = os.path.join(mdir, ind)
                # The song's future location
                new_path = os.path.join(stat_mdir, ind)
                os.rename(cur_path, new_path)
                print("YTR.ripper.downloader.Cleaner renamed", ind,
                      " Now it's @ --> ", new_path)

    @staticmethod
    def destroyer():
        """
            Step 2:
                Remove anything in the outer music dir
                 that does NOT have ".mp3" in its last 4 letters
        """
        mdir = file_helpers.music_dir()
        getall = file_helpers.all_files(mdir)
        for ind in getall:
            this_song = os.path.join(mdir, ind)
            print(this_song)

            # Make sure mp3 is NOT in filename && it's not a directory
            if ("mp3" not in ind[-4:]) and (not os.path.isdir(this_song)):
                os.remove(this_song)
                yield """ YTR.ripper.downloader.Cleaner.destroyer() has removed --> %s """\
                      % this_song


def test_dl():
    northlane = "https://www.youtube.com/watch?v=IjMuhtDkN7o"
    north_video = Dl(link=northlane)
    return north_video.song_dl()
# print(my_test())
# print(os.getcwd())
