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


**How to Use**

To run via the **command line**, run the meme.py file in the 
python interpreter (python 3 required).  This requires a path 
argument which is the image that will be used for the meme,
and two optional arguments (--body and --author) to specify 
a custom quote.  If they are not specified, a random quote 
from the library will be used instead.  

To start the **flask web app**, 


**Structure and Modules**



