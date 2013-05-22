# Tiles2BigMap

## Installation

Tiles2BigMap needs PIL.
install PIL via `pip install PIL`
or on OSX `brew install pil`

## Using

* Go to [BigMap](http://openstreetmap.gryph.de/bigmap.html) Select an area, an click submit.
* Copy URL
* start Tiles2BigMap `python image.py -u '<BigmapURL>'`
* if you installed PIL via brew, then you have to type in something like this `PYTHONPATH=/usr/local/Cellar/pil/1.1.7/lib/python2.7/site-packages/ python image.py -u '<BigmapURL>'`