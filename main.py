"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import png
from flask import Flask, send_file
import StringIO
from noise import snoise2, pnoise2
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/simplex.png')
def simplexmap():
    """Return a simple image."""
    img_io = StringIO.StringIO()
    s = []
    for x in xrange(500):
        row=[]
        for y in xrange (800):
            pixel=snoise2(x,y)
            #print "%r " % pixel
            pixel=int((pixel+1)/2*255)
            row.append(pixel)
        s.append(row)

    s = map(lambda x: map(int, x), s)
    #draw a simple grayscale gradient png
    w = png.Writer(len(s[0]), len(s),greyscale=True)
    w.write(img_io,s) 
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/perlin.png')
def perlinmap():
    """Return a simple image."""
    img_io = StringIO.StringIO()
    s = []
    for x in xrange(500):
        row=[]
        for y in xrange (800):
            pixel=pnoise2(x,y)
            #print "%r " % pixel

            pixel=int((pixel+1)/2*255)
            row.append(pixel)
        s.append(row)

    s = map(lambda x: map(int, x), s)
    #draw a simple grayscale gradient png
    w = png.Writer(len(s[0]), len(s),greyscale=True)
    w.write(img_io,s) 
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


if __name__ == '__main__':
    app.debug = True
    app.run()
