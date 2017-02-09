# Python imports
import os
from YTR.models import YtrConfig


# Return files in a certain directory
def all_files(which_dir):
    for songs in os.fwalk(which_dir):
        return songs[2]


# Get path for FFmpeg
def find_ffmpeg():
    for my_files in os.listdir(YtrConfig.main_dir):
        if my_files == "ffmpeg":
            return os.path.abspath(my_files)
        else:
            return False


# Move files with "move_me" to music dir
# Don't move the ffmpeg binary
def clean_dir(move_me):
    for filename in os.listdir(os.getcwd()):
        if move_me in filename and ("ffmpeg" not in filename):
            if ".mkv" in filename[-4:]:
                os.rename(filename,
                          os.path.join("music", filename))
            elif ".mp4" in filename[-4:]:
                os.rename(filename,
                          os.path.join("music", filename))
            elif ".webm" in filename[-4:]:
                os.rename(filename,
                          os.path.join("music", filename))
                # print(filename, end='')
            elif ".mp3" in filename[-4:]:
                os.rename(filename,
                          os.path.join("music", filename))
            else:
                pass
        else:
            return False
