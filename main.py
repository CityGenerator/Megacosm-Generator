"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import png
from flask import Flask, send_file
import StringIO
import random
from noise import snoise2, pnoise2,snoise3
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
#   random.seed(2)
    offset=random.randint(1,100)
    s = []
    zoom=260.0
    waterline=145
    for x in xrange(500):
        row=[]
        for y in xrange (800):
            
            pixel=snoise2(offset+x/zoom,offset+y/zoom,  4, 0.4,2.0, 500/zoom*4, 800/zoom, 1 )
            #noise2(x, y, octaves=1, persistence=0.5, lacunarity=2.0, repeatx=None, repeaty=None, base=0.0) return simplex noise value for specified 2D coordinate.

            pixel=int((pixel+1)/2*255-1)

            if (pixel <waterline):
                row.append(max(pixel/2,0))
                row.append(max(pixel/2,0))
                row.append(255-max(pixel/4,0))
            else:
                pixel=(pixel-waterline)* 255/waterline
                row.append(54+pixel)
                row.append(54+pixel)
                row.append(pixel)
        s.append(row)

    #draw a simple grayscale gradient png
    w = png.Writer(len(s[0])/3, len(s),greyscale=False, alpha=False)

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
