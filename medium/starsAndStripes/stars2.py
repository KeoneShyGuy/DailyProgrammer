# https://redd.it/589txl

from PIL import Image, ImageDraw, ImageFilter, ImageFont
from math import cos, sin, pi, radians
def make_gram(sides):
	dimension = 2**9
	im = Image.new("RGB", (dimension, dimension), "white")
	draw = ImageDraw.Draw(im)
	startPoint = (im.size[0]*.5, im.size[1]*.5)
	startAngle = 3*pi/2
	allPoints = []
	points = sides
	increments = (2*pi) / points
	lineLength = int(dimension / 2 / 1.1)
	for i in range(points + 1):
		x = startPoint[0] + lineLength*cos(startAngle + i*increments)
		y = startPoint[1] + lineLength*sin(startAngle + i*increments)
		allPoints.append((x, y))
		
	for idx,point in enumerate(allPoints):
		if (points%2) == 0:
			endIdx = points / 2 - 1
			destin = (idx+endIdx)%points
		else:
			endIdx = points / 2
			destin = (idx+endIdx)%points
		draw.line((allPoints[destin], point),fill="red", width=1)

	draw.line((allPoints), fill="blue", width=1)
	
	del draw
	fileName = "{}-agram.png".format(points)
	
	im.save(fileName)

for i in range(5, 6):
	make_gram(i)