from YTR import app
import subprocess


def open_browser():
    subprocess.run("open 127.0.0.1:5100", shell=True)

# open_browser()
if __name__ == '__main__':
    app.run(debug=True, port=5100)
