# Created by RaulByte
# Roblox Image Parser No. 2

import urllib.request
import io
from PIL import Image

import flask
import requests
from flask import jsonify, request, send_file

app = flask.Flask(__name__)
app.config['DEBUG'] = True


# Home Page
@app.route('/', methods=['GET'])
def home():
    return 'Made by RaulByte. If you don\'t know how to use me, check me up on YouTube.'


@app.route('/get')
def getImage():
    # Get image URL parameter
    imageURL = request.args.get('image_url')
    imageWidth = int(request.args.get('width'))
    imageHeight = int(request.args.get('height'))

    # Return an error message if any of the parameters are missing
    if None in {imageURL, imageWidth, imageHeight}:
        return 'A parameter is missing: Check for {"image_url", "width", "height"}'

    # Store all of the Hex Color data (ff00ff)
    pixelList = ''

    print("Request Data: \n Link: {imageURL}\n Dimensions: {width}x{height}".format(imageURL=imageURL, width=imageWidth, height=imageHeight))

    urlData = urllib.request.urlopen(imageURL)
    imageData = Image.open(io.BytesIO(urlData.read())).resize((imageWidth, imageHeight), Image.BILINEAR) #.rotate(90)
    
    imageRGB = imageData.convert('RGB')
    
    for column in range(imageData.size[0]):
        for row in range(imageData.size[1]):
            r = imageRGB.getpixel( (column, row) )[0]
            g = imageRGB.getpixel( (column, row) )[1]
            b = imageRGB.getpixel( (column, row) )[2]

            #hexValue = "#%02x%02x%02x" % (r, g, b)
            hexValue = '#{:02x}{:02x}{:02x}'.format( r, g, b )

            #print(hexValue)
        
            pixelList += hexValue
        pixelList+='\n'
    return jsonify(pixelList)
    

app.run()
