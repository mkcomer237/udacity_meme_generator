**Meme Generator (from the Udacity Intermediate Python Nanodegree)**

This project implements a basic meme generator that pairs images with 
quotes to form a meme.  It was the final project in the Large Codebases
with Libarars portion of the Udacity Intermediate Python Nanodegree.  
It can be run as a command line utility or a simple flask web app, 
and allows the user to specify an image on disk or on the web, which 
will be paired with one of the random quotes in the included quote 
library (or a user specified quote).  The final meme will be the 
original image, resized, and with the quote body and author displayed 
on it.  


**Setup**

python 3.9
python3 -m pip install -r requirements.txt
also requires installing the xpdfreader cli utility for reading pdfs

**How to Use**

To run via the **command line**, run the meme.py file in the 
python interpreter (python 3 required).  This requires a path 
argument which is the image that will be used for the meme,
and two optional arguments (--body and --author) to specify 
a custom quote.  If they are not specified, a random quote 
from the library will be used instead. Example:
python3 meme.py _data/photos/dog/xander_1.jpg

To start the **flask web app**, run: 
export FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

Then open the local server started by flask in a browser
to use the app.  The app generates random memes based on the 
stock library, and also allows linking to any image on the web.


**Structure and Modules**

The project implements two interfaces
app.py is the flask app
meme.py is a cli interface
Both of these rely on the MemeEngine and QuoteEngine modules 
to generate the meme combination of image and text.  
The make_meme method from MemeEngine takes in a quote 
body and author as well as an image and comines them into 
the final meme.  The QuoteEngine implements a QuoteModel object
to store the quote body and author, and also a set of ingestor
classes to handle importing quotes stored in different data
types.  The Ingestor object encapsulates all of these 
and automatically chooses the right ingestor for the file 
extension.  

