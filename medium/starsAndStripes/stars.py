# https://redd.it/589txl

from PIL import Image, ImageDraw
from math import cos, sin, pi
from random import randint
dimension = 2**10

im = Image.new("RGB", (dimension, dimension), "white")
draw = ImageDraw.Draw(im)
startPoint = (im.size[0]*.5, im.size[1]*.05)
allPoints = [startPoint]
for i in range(6):
	print i
	print allPoints[-1]
	x = allPoints[-1][0] 
	x += randint(-32, 32)
	y = allPoints[-1][1]
	y += randint(0, 128)
	allPoints.append((x, y))
		
print allPoints
draw.line((allPoints), fill="blue", width=4)
draw.polygon((allPoints), outline="red")

del draw

im.save("stars.png")

