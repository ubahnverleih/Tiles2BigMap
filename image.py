from PIL import Image
import urllib2

# permalink for this map: http://openstreetmap.gryph.de/bigmap.cgi?xmin=8815&xmax=8818&ymin=5480&ymax=5482&zoom=14&scale=256&baseurl=http%3A%2F%2Ftile.openstreetmap.org%2F!z%2F!x%2F!y.png

xmin = 8805;
xmax = 8808;
ymin = 5490;
ymax = 5492;
zoom = 14;
scale = 256;
url = "http://tile.openstreetmap.org/!z/!x/!y.png";

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
		tileurl = 'http://tile.openstreetmap.org/'+str(zoom)+'/'+str(x)+'/'+str(y)+'.png'

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



mainimage.save("./karte.png","PNG")
mainimage.show()