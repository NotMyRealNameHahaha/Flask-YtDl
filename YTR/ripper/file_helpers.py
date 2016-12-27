# Python imports
import os

# Dependencies
# import ffmpy
# Project imports
# from convert import convert.converter as converter
import YTR.convert


# Directory helpers
# -----------------#
# Current working directory
def get_cwd():
    return os.getcwd()


# Get the 'music' directory
def music_dir():
    for my_dirs in os.listdir(get_cwd()):
        if "music" in my_dirs:
            return os.path.abspath(my_dirs)
        else:
            pass


# Return files in a certain directory
def all_files(which_dir):
    for songs in os.fwalk(which_dir):
        return songs[2]


# Get path for FFmpeg
def find_ffmpeg():
    for my_files in os.listdir(os.getcwd()):
        if my_files == "ffmpeg":
            return os.path.abspath(my_files)
        else:
            return False


# Move files with "move_me" to music dir
# Don't move the ffmpeg binary
def clean_dir(move_me):
    for filename in os.listdir(get_cwd()):
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
        return False


# Check the cwd/music folder for non-MP3 files
# If a non-mp3 file exists, run it through converter
def mp_check():
    for my_files in os.listdir(music_dir()):
        if ".mp3" not in my_files[-4:]:
            print(".mp3 is not in -> " + my_files)
            my_converter(my_files)
            # print(os.listdir(music_dir()))


# Uses converter module to connect to FFmpeg && convert to mp3
def my_converter(infile):
    filename, file_extension = os.path.splitext(infile)
    better_outfile = str(filename + '.mp3')

    c = YTR.convert.Converter(
        ffmpeg_path=find_ffmpeg()
    )
    # Set the config for converter
    options = {
        'format': 'mp3',
        'audio': {
            'codec': 'mp3',
            'bitrate': '22050',
            'channels': 1
        }
    }
    conv = c.convert(infile=infile,
                     outfile=better_outfile,
                     options=options
                     )
    # return (x for x in conv)
    print("file_helpers -> converter -> conv == ", conv)
    return (x for x in conv)


