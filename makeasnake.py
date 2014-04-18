'''
Procedural Snakeskin image generator

author: J. Adrian Herbez
website: http://www.adrianherbez.net


'''

import sys, math
import Image, ImagePalette, ImageDraw
import random

def ConvertColor(input,base1,base2,spread):
	input = (input - input*spread)
	newColor = [0,0,0]
	for i in range(0,3):
		newColor[i] = base2[i] * input + (base1[i] * (1-input))

	return (newColor[0],newColor[1],newColor[2])

def MakeSnakeSkin(argv):
	print('making snakeskin image')
	
	COLOR_BACK = (128,200,128)
	COLOR_FORE = (0,0,0)
	
	COLOR_BACK = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	COLOR_FORE 	= (COLOR_BACK[0] * 0.1,COLOR_BACK[1]*0.1,COLOR_BACK[2]*0.1)
	COLOR_SPOT	= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	spot_out	= random.random() / 5
	COLOR_FORE	= (COLOR_SPOT[0] * spot_out, COLOR_SPOT[1] * spot_out, COLOR_SPOT[2] * spot_out)
	COLOR_BELLY	= (min(COLOR_BACK[0] * 1.7,255),min(COLOR_BACK[1]*1.7,255),min(COLOR_BACK[2]*1.7,255))
	
	COLOR_SCALES	= (128,128,128)
	
	HEIGHT 	= 512
	WIDTH 	= 256
	Cntr	= math.floor(WIDTH * 0.5)
	Qrtr	= math.floor(WIDTH * 0.15)
	Belly 	= math.floor(WIDTH * 0.15)

	sMin	= math.floor(WIDTH * 0.1)
	sMax	= sMin + 20

	Reps	= random.randint(1,10) * 6.28 

	vert_speed 	= 0.1
	offset		= 0.5
	
	MAX_DISP = 20
	
	T = random.random() * MAX_DISP 
	T2 = random.random() * MAX_DISP * 0.5

	vert_speed = random.random() * 0.1
	offset = random.random()
	spread  = random.random() * 0.5

	outfile = 'sskin.bmp'
	out = Image.new("RGB",(WIDTH,HEIGHT))
	draw = ImageDraw.Draw(out)
	draw.rectangle([0,0,WIDTH,HEIGHT],fill=COLOR_BACK)
	
	for i in range(0,HEIGHT):
		max = abs(math.sin(i*vert_speed) * 20)
		max += abs(math.cos(i*vert_speed*offset) * 10)		
		max_main = math.floor(max - T)

		if (max_main > 0): 
			#draw.line([(64-max_main,i),(max_main+64,i)],fill=COLOR_FORE)
			for j in range(0,max_main):
				ColorTemp = ConvertColor((j/max_main),COLOR_SPOT,COLOR_FORE,spread)
				draw.point((Cntr-j,i),fill=ColorTemp)
				draw.point((Cntr+j,i),fill=ColorTemp)
		
		max_2 = abs(max_main-MAX_DISP)
		if (max_2 > 0):
			for j in range(0,max_2):
				ColorTemp = ConvertColor((j/max_2),COLOR_SPOT,COLOR_FORE,spread)
				draw.point(((Cntr-Qrtr)-j,i),fill=ColorTemp)
				draw.point(((Cntr-Qrtr)+j,i),fill=ColorTemp)

				draw.point(((Cntr+Qrtr)-j,i),fill=ColorTemp)
				draw.point(((Cntr+Qrtr)+j,i),fill=ColorTemp)

		for j in range(0,Belly):
			draw.point((0+j,i),fill=COLOR_BELLY)
			draw.point((WIDTH-j,i),fill=COLOR_BELLY)
	
	# add in lines for the scales
	for i in range(0,HEIGHT):
		x_sin = math.sin(i * 0.2)
		x = x_sin * 10 + sMin
		y = i
		draw.point((x,y),fill=COLOR_SCALES)
		draw.point(((WIDTH-x),i),fill=COLOR_SCALES)		
		if (abs(1-x_sin) < 0.015):
			draw.line((sMin+10,i,WIDTH-sMin-10,i),fill=COLOR_SCALES)		
		if (abs(-1-x_sin) < 0.015):
			draw.line((0,i,sMin-10,i),fill=COLOR_SCALES)
			draw.line((WIDTH-sMin+10,i,WIDTH,i),fill=COLOR_SCALES)

	out.save(outfile,"BMP")


if (__name__ == "__main__"):
	MakeSnakeSkin(sys.argv[1:])
