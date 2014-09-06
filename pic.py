import Image 
import ImageFilter
import ImageEnhance
from pytesser import *

def clean(text):
	rep={'O':'0',
	'J':'1','L':'1',
	'Z':'2',
	'S':'8'}
	for r in rep:
		text=text.replace(r,rep[r])
	string=''
	numbers='0123456789'
	for s in text:
		if s in numbers:
			string+=s
	string=string[:-2]+'.'+string[-2:]
	return string

def get_string(file):
	im=Image.open(file)
	x,y=im.size
	box=(12,0,x,y)
	# im = im.crop(box)
	Lim  =  im.convert('L')
	threshold  =   200 
	table  =  []
	for  i  in  range( 256 ):	
		if  i  <  threshold:
			table.append(0)
		else :
			table.append( 1 )
	bim  =  Lim.point(table,'1')
	bim=bim.convert('L')
	bim=bim.filter(ImageFilter.DETAIL)
	x,y=bim.size
	bim=bim.resize((x*2,int(y*1.3)))
	bim.show()
	text= image_to_string(bim)
	text=clean(text)
	print text
if __name__ == '__main__':
	get_string('1057881.18.png')
