from PIL import Image
import urllib2
from urlparse import urlparse, parse_qs
from optparse import OptionParser 



#parse arguments
parser = OptionParser()

parser.add_option("-u", "--url", dest="url")
parser.add_option("-o", "--outputfile", dest="output")

(optionen, args) = parser.parse_args()



# permalink for this map: http://openstreetmap.gryph.de/bigmap.cgi?xmin=8815&xmax=8818&ymin=5480&ymax=5482&zoom=14&scale=256&baseurl=http%3A%2F%2Ftile.openstreetmap.org%2F!z%2F!x%2F!y.png
"""
xmin = 8805;
xmax = 8808;
ymin = 5490;
ymax = 5492;
zoom = 14;
scale = 256;
tileserver = "http://tile.openstreetmap.org/!z/!x/!y.png"; #osm
#tileserver = "http://otile1.mqcdn.com/tiles/1.0.0/map/!z/!x/!y.jpg"; #mapquest
"""

url = optionen.url

#parse bigmap URL
urlparams = parse_qs(urlparse(url).query)
xmin = int(urlparams["xmin"][0]);
xmax = int(urlparams["xmax"][0]);
ymin = int(urlparams["ymin"][0]);
ymax = int(urlparams["ymax"][0]);
zoom = int(urlparams["zoom"][0]);
try:
	scale = int(urlparams["scale"][0]);
except:
	scale = 256
tileserver = urlparams["baseurl"][0];


#Aus tileserver URL und tileinfos wird tileURL generiert
def getTileURL(tileserver, x, y, z):
	tileserver = tileserver.replace("!x",str(x))
	tileserver = tileserver.replace("!y",str(y))
	tileserver = tileserver.replace("!z",str(z))
	return tileserver






width = (xmax-xmin)*scale;
height = (ymax-ymin)*scale;

size = width, height

mainimage = Image.new("RGB", size);

for x in range(xmin, xmax):
	xanz = x - xmin; #das wie vielte Bild (x)
	for y in range(ymin, ymax):
		yanz = y - ymin; #das wie vielte Bild (y)

		#header bauen - Useragent
		headers = { 'User-Agent' : 'Tiles2BigMap' }

		#url bauen
		tileurl = getTileURL(tileserver,x,y,zoom)# 'http://tile.openstreetmap.org/'+str(zoom)+'/'+str(x)+'/'+str(y)+'.png'

		#request
		req = urllib2.Request(tileurl, None, headers)

		u = urllib2.urlopen(req)
		#Tile speichern
		localFile = open('./tmp/'+str(zoom)+'-'+str(x)+'-'+str(y)+'.png', 'w')
		localFile.write(u.read())
		localFile.close()


		#in Bild einfuegen
		b = Image.open('./tmp/'+str(zoom)+'-'+str(x)+'-'+str(y)+'.png')

		mainimage.paste(b,(xanz*scale,yanz*scale,(xanz+1)*scale,(yanz+1)*scale))


#output

try:
	if(len(optionen.output)>0):
		outputfilename = optionen.output
	else:
		outputfilename = "./karte.png"
except:
	outputfilename = "./karte.png"

mainimage.save(outputfilename,"PNG")
mainimage.show()



