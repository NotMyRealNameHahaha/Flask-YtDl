# Flask-YtDl
A convenient marriage of Flask and Youtube-dl.
Flask-YtDl is NOT a Flask Extension.  It is simply a Web interface to [youtube-dl](https://github.com/rg3/youtube-dl), and it uses [Flask](http://flask.pocoo.org/) to make this happen.
Additionally, it serves as a simple example of how to use the common features of Flask.

# Getting Started
### Versions
The OSX version and Linux version only differ in two ways:
- FFmpeg binaries
- The 'open_browser()' function


### Requirements
<<<<<<< HEAD
Flask-YtDl is written in **Python 3.6.0** & has not been tested in other versions; however, minimal compatability issues may occur if using Python 2.x.
=======
Flask-YtDl is written in **Python 3.5.2** & has not been tested in other versions.  If you would like to rewrite it to improve compatability, please do.
Dependencies can be found in requirements.txt.
>>>>>>> 004d6d9d06eaa42327b33e664e66e10573dd2b2e

### Installation
Clone the git repo
```shell
git clone https://github.com/NotMyRealNameHahaha/Flask-YtDl.git
```
Create your virtualenv, activate it, & download dependencies
```shell
virtualenv -p /usr/bin/python3.5 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start it up
python runserver.py

### Main Files
The YTR folder contains most of the files that bring this application to life.  YTR = YouTube Ripper :)



# Features
Flask-YtDl basically downloads videos off of Youtube, then runs those videos through FFmpeg (which is included) to extract the highest quality MP3 file from each video.  Immediately after conversion, the videos file are deleted.  

To be 100% clear, this means that Flask-YtDl does **not** keep videos, it only rips mp3s from Youtube videos.

While this process is a bit inefficient, it mitigates any inconsistencies that can occur with just using youtube-dl.  As such, you should not use anything like this in a production setting.  But it's perfect for a local app.

<<<<<<< HEAD
- Download & conversion processes run asynchronously
=======
>>>>>>> 004d6d9d06eaa42327b33e664e66e10573dd2b2e
- Supports multiple uploads.  Just click the "+" button on the home page.
- Creates a directory of all songs you've downloaded.
  - You can download them like you would from any other site
  - Delete files from this directory to save harddrive space
  - These mp3 files can be found in YTR/static/music
- Asynchronously verifies URLS
  - Try it: On the home page, enter a url.  Do not submit the form, just click anywhere else on the page.  Shortly thereafter a message will pop up with either 1. The name of the video **or** 2. A message asking to double check the URL

# Extra Features
<<<<<<< HEAD
When you start Flask-YtDl, it runs on http://127.0.0.1:5100.  Flask apps, by default, run on port 5000.  This feature allows you to keep Flask-YtDl out of the way.  If it gets in your way, or you just want to turn it off, you have two options:
1. Shut down the server by going visiting http://127.0.0.1:5000/shutdown
    You'll notice the very prominent "shutdown server" button as well
2. 
=======
When you start Flask-YtDl, it runs on http://127.0.0.1:5100.  Flask apps, by default, run on port 5000 (vs. 5100).  This feature allows you to keep Flask-YtDl out of the way.  If it gets in your way, or you just want to turn it off, you have two options:
1. Shut down the server by going visiting http://127.0.0.1:5000/shutdown
2. Open terminal, change to the Flask-Tube directory and (on Linux) type './shutdown.sh' and hit enter
>>>>>>> 004d6d9d06eaa42327b33e664e66e10573dd2b2e

**runserver.py** includes a convenient function to open your default browser for you.  To add this functionality, simply change
```python
# open_browser()
if __name__ == '__main__':
    app.run(debug=True, port=5100)
```
To:
```python
open_browser()
if __name__ == '__main__':
    app.run(debug=True, port=5100)
```


<<<<<<< HEAD
=======
# Customizing Flask-YtDl
Feel free to tear into the code, you'll find comments throughout every file.
- For your convenience, most of the Python functions also have a print(something) feature commented out.  Just remove the # to see what's happening behind the scenes
- JS && CSS are NOT minified and contain a ton of comments
If you create something awesome with this, fork it, pull it, whatever you want to do, and I'll add a link to your awesomeness

>>>>>>> 004d6d9d06eaa42327b33e664e66e10573dd2b2e

# Limitations
- Only downloads mp3s
- Does not play music.  Other applications already do an amazing job at this.
<<<<<<< HEAD
- Admittedly, the download/conversion processes are slow, though it's not immediately evident since those processes run in the background.
=======
- Admittedly, the download & conversion processes are slow; however, they are extremely reliable.
>>>>>>> 004d6d9d06eaa42327b33e664e66e10573dd2b2e


# Credit Where Credit is Due
[Flask- A Python Microframework](http://flask.pocoo.org/)
<br>
[youtube-dl](https://github.com/rg3/youtube-dl)
<br>
[FFmpeg](https://www.ffmpeg.org/)
<br>
[FFmpeg static binaries](https://github.com/eugeneware/ffmpeg-static) by @eugeneware

<<<<<<< HEAD
=======

>>>>>>> 004d6d9d06eaa42327b33e664e66e10573dd2b2e
