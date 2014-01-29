"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import png
from flask import Flask,  send_file
import StringIO
#from noise import snoise2  <-- troublemaker
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/map.png')
def hellomap():
    """Return a simple image."""
    img_io = StringIO.StringIO()
    s = [
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011',
        '000000000000000000000000000000000000',
        '000000000000000000000000000000000000',
        '000000000000000000000000000000000000',
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011',
        '101011010100110010010011110010010011']
    s = map(lambda x: map(int, x), s)
    #draw a simple grayscale gradient png
    w = png.Writer(len(s[0]), len(s), greyscale=True,bitdepth=2)
    w.write(img_io,s) 
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

