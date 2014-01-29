"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import png
from flask import Flask,  send_file
import StringIO
from noise import pnoise2
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

    w = png.Writer(255, 1, greyscale=True)
    w.write(img_io, [range(256)])
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404
