
Running Flask-YtDl on Mac OS requires one of the following:

1. FFmpeg must be installed
2. Replace the FFmpeg in the parent directory with the version of FFmpeg in this directory.

Example of option 2:
# Change to the Flask-YtDl directory before doing this
$ rm ffmpeg
$ mv OSX/ffmpeg $pwd

