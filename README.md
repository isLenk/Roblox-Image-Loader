# Roblox Image Loader

The project folder for my video: https://www.youtube.com/watch?v=4mphsOSH6YM

## Getting Started

### Prerequisites
The project will not function properly without [Python](https://www.python.org/) and Roblox Studio

### Libraries Required:
Use [PIP](https://www.liquidweb.com/kb/install-pip-windows/) to install these libraries
  * [urllib](https://docs.python.org/3/library/urllib.html)
  * [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
  * [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)
  * [requests](https://requests.readthedocs.io/en/master/user/install/#install)

### Instructions
1. Launch the Python File. You should see something like "Runing on http://127.0.0.1:5000/"
2. Open the Roblox File
3. Look for an image to use on Google. 
  > Right click the image and click 'View Image'
  You may want to open the image up before right clicking it, that way you get the largest size possible
4. Run this program in Roblox Command

```lua
_G.imageURL = "Enter URL here"
_G.dimensions = {200, 200}
_G.pixelLength = 1
loadstring(game.ServerStorage.Imager.Source)()
```

  > If you cannot find Command, right click the tabs (Where Home/Model/Test/View/Plugins are), then select the 'Command' option
5. Fall into the pits of degeneracy as your curiousity overtakes your innocence.
